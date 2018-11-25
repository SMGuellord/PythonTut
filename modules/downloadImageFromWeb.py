import random
import urllib.request


def downloadWebImage(url):
    name = random.randrange(1,1000)
    fullname = str(name) +".jpg"  #str convert number to string value
    urllib.request.urlretrieve(url, fullname)


downloadWebImage("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLuQZO9YQzSN1RKGd2Zw80QqByf4mPdQMwwYwh7tPxo9RL6A7G")