import re
import requests

MAX_PAGE = 143
urlformat = 'http://www.codeforces.com/ratings/page/%d'

usernames = []

for i in range(1, MAX_PAGE+1):
    print 'processing page %d...' % i

    r = requests.get(urlformat % i)
    user_data = re.findall(u'(?s)<td style="text-align:left;padding-left:1em;\">.*?<a.*?>(.*?)</a>', r.text)
    for username in user_data:
        username = re.sub(u'<.*?>', '', username)
        usernames.append(username)

f = open("username", "w")
for username in usernames:
    f.write("%s\n" % username)
f.close()
