import sys
from Queue import Queue
import re
import threading
import requests

output_lock = threading.Lock()
print_lock = threading.Lock()
cnt_lock = threading.Lock()
file_lock = threading.Lock()

pattern = re.compile(u'(?s)<td style="text-align:left;padding-left:1em;\">.*?<a.*?>(.*?)</a>')
pattern2 = re.compile(u'<.*?>')
class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global page_cnt, MAX_PAGE
        cnt_lock.acquire()
        page_cnt += 1
        self.page_cnt = page_cnt
        cnt_lock.release()
    def run(self):
        if (self.page_cnt > MAX_PAGE):
            return
        print_lock.acquire()
        print_lock.release()
        r = requests.get(urlformat % self.page_cnt)
        user_data = re.findall(pattern, r.text)
        for username in user_data:
            username = re.sub(pattern2, '', username)

            output_lock.acquire()
            usernames.append(username)
            output_lock.release()
        print 'processed page %d...' % self.page_cnt

        new_worker()

threads = Queue()
def new_worker():
    worker = Worker()
    worker.start()
    threads.put(worker)

MAX_PAGE = 143
page_cnt = 0
urlformat = 'http://www.codeforces.com/ratings/page/%d'

usernames = []
max_connections = 6
if len(sys.argv) == 2:
    max_connections = int(sys.argv[1])

for i in range(max_connections):
    new_worker()
while not threads.empty():
    t = threads.get()
    t.join()

f = open("username", "w")
for username in usernames:
    f.write("%s\n" % username)
f.close()
