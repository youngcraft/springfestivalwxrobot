#!/usr/bin/python
# coding: utf-8

import os
import time
from wxpy import *
from time import sleep

'''
bot = Bot()

my_friends = bot.friends()

print type(my_friends)

sex_dict = {'male':0,'female':1}

for friend in my_friends:
    # sexual analysis
    if friend.sex == 1:
        sex_dict['male'] +=1
    elif friend.sex == 2:
        sex_dict['female'] +=1

print sex_dict

province_dict = {}

for friend in my_friends:
    if friend.province not in province_dict.keys():
        province_dict[friend.province] = 0

for friend in my_friends:
    if friend.province in province_dict.keys():
        province_dict[friend.province] +=1

data = []
for key,value in province_dict.items():
    data.append({'name':key,'value':value})
for node in data :
    print node
f = open('weixin.txt','w+')
f.write(data)

# signature clean and record
import re
for friend in my_friends:
    print friend

'''

print os.getcwd()
bot = Bot(cache_path=os.getcwd()+'/tmp')
my_friend = bot.friends()
myself = bot.self
bot.file_helper.send('Hello World!')

Tuling.api_key


@bot.register(my_friend)
def reply(msg):
    print '[*] send msg to {}'.format(msg)
    print type(msg)
    # return '[*] received: {} ({})'.format(msg.text, msg.type)
    global bot
    chat_friend = bot.friends()
    # print chat_friend[0]
    # print chat_friend[1]
    localtime =  time.asctime(time.localtime(time.time()))
    # chat_friend[1].send('OK {}'.format(localtime))
    return '好的  {}'.format(localtime)



def hold():
    i = 100000
    while i >= 0:
        sleep(1)
        my_love = my_friend.search(u'ddddd')[0]
        print '[*]send to danlin test msg %d' % i
        my_love.send('I test!\n%d' % i )
        i-=1


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    new_friend = msg.card.accept()
    new_friend.send('哈哈，我自动接受了你的好友请求')

@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        msg.reply('好的')

#hold()j
embed()
