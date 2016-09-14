import requests

fushan_password = ''

s = requests.Session()

url = 'http://www.fushanedu.cn/jxq/jxq.aspx'
#url = 'http://www.fushanedu.cn/jxq/jxq_User_jtzyck.aspx'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
           'Host':        'www.fushanedu.cn',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1'}

cookies = {'studentid': 'value=nothing',
           'ASP.NET_SessionId': 'uujikp55ikpmtc55lmqqpb2f'}

r = s.get(url, cookies=cookies, headers=headers)
print(r.status_code)

url = 'http://www.fushanedu.cn/jxq/jxq.aspx'

cookies = {'studentid': 'value=20161402',
           'ASP.NET_SessionId': 'uujikp55ikpmtc55lmqqpb2f'}

payload = {'login:tbxUserName"': '20161402', 'login:tbxPassword': fushan_password}

r = s.post(url, data = payload, cookies = cookies, headers = headers)
print(r.status_code)


url = 'http://www.fushanedu.cn/jxq/jxq_User.aspx'
r = s.get(url, cookies=cookies, headers=headers)
print(r.status_code)

url = 'http://www.fushanedu.cn/jxq/jxq_User_jtzyck.aspx'
r = s.get(url, cookies=cookies, headers=headers)
print(r.status_code)

with open('output.aspx', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=1024):
        fd.write(chunk)
fd.close

