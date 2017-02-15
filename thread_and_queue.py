#! /usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import threading
import queue
import time
from urllib import request
import re


_DATA = []

FILE_LOCK = threading.Lock()
SHARE_Q = queue.Queue()
#创建一个“队列”对象
_WORKER_THREAD_NUM = 3


class MyThread(threading.Thread):
#继承父类threading.thread

    def __init__(self, func):
        super(MyThread, self).__init__()
        #调用父类的构造函数
        self.func = func

    def run(self):
        self.func()


def worker():
    global SHARE_Q
    while not SHARE_Q.empty():
        #如果队列为空，返回True,反之False
        url = SHARE_Q.get()
        #将一个值从队列中取出
        my_page = get_page(url)
        find_title(my_page)
        time.sleep(1)
        SHARE_Q.task_done()
        # 在完成一项工作之后，task_done() 函数向任务已经完成的队列发送一个信号


def get_page(url):
    try:
        my_page = request.urlopen(url).read().decode("utf-8")
    except request.URLError as e:
        if hasattr(e, "code"):
            #hasattr(object, name) -> bool
            #判断object中是否有name属性，返回一个布尔值。
            print("The server couldn't fulfill the request.")
            print("Error code: %s" % e.code)
        elif hasattr(e, "reason"):
            print("We failed to reach a server. Please check your url and read the Reason")
            print("Reason: %s" % e.reason)
    return my_page

def find_title(my_page):
    temp_data = []
    movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
    for index, item in enumerate(movie_items):
        #对一个列表或数组既要遍历索引又要遍历元素
        if item.find("&nbsp") == -1:
            temp_data.append(item)
    _DATA.append(temp_data)


def main():
    global SHARE_Q
    threads = []
    douban_url = "http://movie.douban.com/top250?start={page}&filter=&type="
    for index in range(10):
        SHARE_Q.put(douban_url.format(page = index * 25))
    for i in range(_WORKER_THREAD_NUM):
        thread = MyThread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    SHARE_Q.join()
    with open("movie.txt", "w+") as my_file:
        for page in _DATA:
            for movie_name in page:
                my_file.write(movie_name + "\n")
    print("okokokokokokooookkk!!!")

if __name__ == '__main__':
    main()




