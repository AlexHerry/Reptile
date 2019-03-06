import socket
import urllib.request
import urllib.parse
import urllib.error
import urllib.robotparser
import http.cookiejar

url = 'http://httpbin.org/post'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Host': 'httpbin.org'
}
value = {
    'name': 'Alex',
    'database': 'test'
}
proxy_handler = urllib.request.ProxyHandler({
#    'http': '112.85.174.217:9999',
    'https': '116.209.53.42:9999'
})
#opener = urllib.request.build_opener(proxy_handler)
filename = 'cookie.txt'

try:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url('https://www.baidu.com/robots.txt')
    rp.read()
    print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/'))
    #   word = '你好'
    #   data = urllib.parse.urlencode(value)
    #   url = 'http://www.baidu.com?wd='
    #   respon = url + urllib.parse.quote(word)
    #   new_url = urllib.parse.unquote(respon)
    #   print(new_url)
    #   print(respon)
    #   print(urllib.parse.urljoin('http://www.baidu.com/index.html','http://www.baidu.com'))
    #   new = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    #   result = urllib.parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
    #   print(type(result), result, len(result),sep='\n')
    #   print(type(new), new, len(new),sep='\n')
    #   res = urllib.parse.urlunparse(['https', 'www.baidu.com', '', '', '', ''])
    #   print(res)
    #   cookie = http.cookiejar.LWPCookieJar(filename)
    #   cookie.load(ignore_discard=True, ignore_expires=True)
    #   handler = urllib.request.HTTPCookieProcessor(cookie)
    #   opener = urllib.request.build_opener(handler)
    #   response = opener.open('https://www.baidu.com')
    #   cookie.save(ignore_discard=True, ignore_expires=True)
    #   for item in cookie:
    #       print(item.name + '=' + item.value)
    #   data = bytes(urllib.parse.urlencode(value), encoding='utf-8')
    #   req = urllib.request.Request(url, data=data, method='post', headers=headers)
    #   response = urllib.request.urlopen(req)
    #   print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
else:
    print('Successful Request')
#  print(response.read().decode('utf-8'))
