import urllib.request


url = 'http://www.ip138.com/'
# 参数是一个字典{'类型':'代理ip:端口号'}
proxy_support = urllib.request.ProxyHandler({'http': '117.191.11.72:8080'})
# 定制，创建一个 opener
opener = urllib.request.build_opener(proxy_support)
# 安装opener
urllib.request.install_opener(opener)
# 调用opener
response = urllib.request.urlopen(url)

html = response.read().decode('')
print(html)