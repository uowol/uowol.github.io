import datetime as dt
import os.path

# Get what date is it today.
now = dt.datetime.now()
nowdate = now.strftime('%Y-%m-%d')
nowtime = now.strftime('%H:%M:%S')
# print(nowtime) # 2020-MM-DD


# Check the post's order
path = 'uowol.github.io/_posts/'
idx = len([name for name in os.listdir(path)]) + 1


# create new file
f = open(path + '%s-post-%d.md' % (nowdate, idx), 'w')
f.write("""---
layout: post
title: ''
description: ''
date: %s %s +0900
categories: 
---""" % (nowdate, nowtime))
f.close()