import threading
import time
import sys
import os
import re

image_urlformat = 'http://codeforces.com/userphoto/title/%s/photo.jpg'

stdout_lock = threading.Lock()
file_lock = threading.Lock()

cnt = 0
def do_with_username(username):
    global cnt
    stdout_lock.acquire()
    cnt += 1
    print "fetching user%d: %s's Avatar" % (cnt, username)
    stdout_lock.release()
    os.system('wget "%s" --quiet --output-document="%s"' % (image_urlformat % username, './images/%s.jpg' % username))

def create_new_worker():
    worker = Worker()
    worker.start()


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #print "i'm created"
    def run(self):
        #print "i'm running!"
        time.sleep(0.05)
        file_lock.acquire()
        username = f.readline().strip('\n')
        file_lock.release()
        if username == '':
            return 0
        do_with_username(username)
        create_new_worker()
        return 0

f = open("username","r")
if not os.path.exists("images"):
    os.makedirs("images")
max_connections = 12
if len(sys.argv) == 2:
    max_connections = int(sys.argv[1])
for i in range(max_connections):
    create_new_worker()
