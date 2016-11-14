import os
import re

f = open("username","r")
image_urlformat = 'http://codeforces.com/userphoto/title/%s/photo.jpg'

#for username in f.readlines():
username = f.readline()
username = username.strip('\n')
os.system('wget "%s" --output-document="%s"' % (image_urlformat % username, './images/%s.jpg' % username))

