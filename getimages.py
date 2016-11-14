import time
import os
import re

f = open("username","r")
image_urlformat = 'http://codeforces.com/userphoto/title/%s/photo.jpg'

if not os.path.exists("images"):
    os.makedirs("images")

cnt = 0
for username in f.readlines():
    username = username.strip('\n')
    cnt += 1
    print "fetching user%d: %s's Avatar" % (cnt, username)
    os.system('wget "%s" --quiet --output-document="%s"' % (image_urlformat % username, './images/%s.jpg' % username))
    time.sleep(0.1)

