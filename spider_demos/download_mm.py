import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/63.0')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    print(html[a:b])
    return html[a:b]


def find_imgs(page_url):
    html = url_open(page_url).decode('utf-8')
    print(html)
    img_addrs = []
    a = html.find('img src=')
    b = html.find('.jpg', a, a+255)
    while a != -1 and b != -1:
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    for each in img_addrs:
        print(each)
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        file_name = each.split('/')[-1]
        with open(file_name) as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='OOXX', pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_mm()
