

def parse_message(data):

    if not isinstance(data, bytes):
        raise TypeError("`data' must be bytes")

    authzid, authcid, passwd = None, None, None

    splitted_data = data.split(b'\0')

    if len(splitted_data) == 3:
        authzid, authcid, passwd = splitted_data

    ret = (
        authzid.decode('utf-8'),
        authcid.decode('utf-8'),
        passwd.decode('utf-8')
        )

    return ret


def format_message(authzid, authcid, passwd):
    ret = b''

    if authzid is not None and not isinstance(authzid, str):
        raise TypeError("`authzid' must be str")

    if not isinstance(authcid, str):
        raise TypeError("`authcid' must be str")

    if not isinstance(passwd, str):
        raise TypeError("`passwd' must be str")

    if authzid is not None:
        ret += authzid.encode('utf-8')

    # NOTE: this NUL is presents anyway, not depending on authzid
    #       value
    ret += b'\0'

    ret += authcid.encode('utf-8')
    ret += b'\0'
    ret += passwd.encode('utf-8')
    return ret


class Server:

    def __init__(self, callback=None):
        self.callback = callback
        self.properties = {}
        return

    def step(self, data):

        if not isinstance(data, bytes):
            raise TypeError("`data' must be bytes")

        ret = None, None

        if len(data) == 0:
            ret = 'need_more', b''
        else:
            res = parse_message(data)
            self.properties['authzid'] = res[0]
            self.properties['authcid'] = res[1]
            self.properties['passwd'] = res[2]
            ret = 'ok', b''

        return ret


class Client:

    def __init__(self, callback=None):
        self.callback = callback
        self.properties = {}
        return

    def step(self, data):

        if not isinstance(data, bytes):
            raise TypeError("`data' must be bytes")

        if self.callback is not None:
            for i in ['authzid', 'authcid', 'passwd']:
                if not i in self.properties:
                    self.properties[i] = self.callback(i)

        ret = 'ok', format_message(
            self.properties['authzid'],
            self.properties['authcid'],
            self.properties['passwd']
            )

        return ret
