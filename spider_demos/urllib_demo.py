import urllib.request as r


if __name__ == "__main__":
    response = r.urlopen("http://www.fishc.com")
    html = response.read()
    print(html.decode("utf-8"))
