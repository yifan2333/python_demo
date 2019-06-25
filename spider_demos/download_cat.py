import urllib.request as r


request = r.Request("http://placekitten.com/500/600")
response = r.urlopen(request)
cat_img = response.read()

with open('cat_500_600.jpg', 'wb') as file:
    file.write(cat_img)

print(response.info())
print(response.geturl())
print(response.getcode())
