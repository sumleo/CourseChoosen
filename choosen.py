import requests
headers={'Accept':'*/*',
'Accept-Encoding':'gzip,deflate',
'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
'Connection':'Keep-Alive',
#抓一下cookie
'Cookie':'',
'Host':'jwxt.sustc.edu.cn',
'Referer':'http://jwxt.xxxxx.edu.cn/jsxsd/xsxkkc/comeInFawxk',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
'X-Requested-With':'XMLHttpRequest'
}
payload={'jx0404id':'选课票据','trjf':'','xkzy':''}
#选课api
request= requests.get(url='http://jwxt.xxxxxx.edu.cn/jsxsd/xsxkkc/fawxkOper',params=payload,headers=headers)
print(request.text)

