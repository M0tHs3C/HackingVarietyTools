import os,sys,requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
hosts = open(sys.argv[1])
hosts = hosts.readlines()
i = 0
for url in hosts:
    hostUrl = hosts[i]
    hostUrl = hostUrl.rsplit(' ')
    i = i + 1
    try:
        print("--Testing: "+ hostUrl[0])
        response = requests.post(hostUrl[0]+ "/xmlrpc.php", verify=False)
        print(response.status_code)
        if response.status_code == 200:
            r = response.text
            print(r)
            if 'XML' in r or 'xml' in r:
                print(hostUrl[0]+"/xmlrpc.php" + " has xmlrpc.php accessible")
        else:
            pass
    except requests.exceptions.SSLError:
        pass
    except requests.exceptions.ConnectionError:
        pass
    

    
