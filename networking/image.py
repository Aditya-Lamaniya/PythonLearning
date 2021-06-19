import urllib.request

url="https://www.webfx.com/blog/images/cdn.designinstruct.com/files/315-mixed_grunge_textures/mixed_grunge_texture_01.jpg"

urllib.request.urlretrieve(url,"imageexample.jpg")
urllib.request.urlretrieve("https://www.webfx.com/blog/images/cdn.designinstruct.com/files/315-mixed_grunge_textures/mixed_grunge_texture_01.jpg","imageex2.jpg")