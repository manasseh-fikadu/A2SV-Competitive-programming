class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            ip = queryIP.split('.')
            for i in ip:
                if not i.isdigit():
                    return 'Neither'
                if len(i) > 1 and i[0] == '0':
                    return 'Neither'
                if int(i) > 255:
                    return 'Neither'
            return 'IPv4'
        elif queryIP.count(':') == 7:
            ip = queryIP.split(':')
            for i in ip:
                if len(i) > 4 or len(i) == 0:
                    return 'Neither'
                for j in i:
                    if not j.isdigit() and not (ord(j) >= 97 and ord(j) <= 102) and not (ord(j) >= 65 and ord(j) <= 70):
                        return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'