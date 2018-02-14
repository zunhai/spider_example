import requests, json
if __name__ == '__main__':
     target = 'http://unsplash.com/napi/feeds/home'
     headers = {'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
     req = requests.get(url=target, headers=headers, verify=False)
     html = json.loads(req.text)
    
     next_page = html['next_page']
     print('下一页地址:',next_page)
     for each in html['photos']:
          print('图片ID:',each['id'])