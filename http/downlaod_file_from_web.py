import urllib

# import requests


urllib.request.urlretrieve('https://source.unsplash.com/random?sig', 'image/')

# for i in range(10):
#     url = 'https://source.unsplash.com/random?sig='+ str(i)
#     resp = requests.get(url=url)
#     file = open('image'+str(i)+'.png', 'wb')
#     print(resp.content)
#     # file.write(resp.content)
#     # file.close()
