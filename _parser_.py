import os
from channel import *
from movie import*
from series import *

tv_name = ""
def read_tvFile_contents(file):
    global tv_name
    tv_name = file
    f = open(file, "rb")

    file = f.read()
    if len(file) == 0:
        print("File is empty")
        os._exit(100)
    f.close()

    return file

memory = []
lines = []

countries = []
tot = []
recognized_group_title = False
def parse_file_contents(file_content):
    global memory, lines, countries, tot, recognized_group_title
    # each line beginning with "#EXTINF:-1 "
    text = file_content.decode()
    lines = text.split("#EXTINF:-1 ")
    item = lines[2]
    s = item.split('"')
    test = ""
    now = False

    for i in s:
        if now == True:
            test += i
            now = False
        if i == " group-title=":
            test += i
            now = True 
    for line in lines:
        buffer = ""
        details = line.split('"')
        for word in details:
            if recognized_group_title:
                tmp = word.split("|")
                buffer = tmp[0]
                #### operate on buffer 
                if handle_country(buffer):
                    #push_the_line(buffer, line)
                    print(buffer)
                    if buffer == '':
                        buffer = word
                    countries.append(buffer)
                recognized_group_title = False 
                x = check_type(details[-1])
                if x == "channel":
                    push_to_channel(buffer, line)
                elif x == "movie":
                    push_to_movie(buffer, line)
                elif x == "series":
                    push_to_series(buffer, line)
                push_the_line(buffer, line)

            if word == " group-title=":
                #buffer += word
                recognized_group_title = True








def handle_country(param):
    if param in countries:
        return False
    return True



def push_the_line(country, info):
    global memory
    for index in memory:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    memory.append(tmp)
    return False

channels_list = []
movies_list = []
series_list = []


def push_to_channel(country, info):
    global channels_list
    for index in channels_list:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    channels_list.append(tmp)
    return True

def push_to_series(country, info):
    global series_list
    for index in series_list:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    series_list.append(tmp)
    return True

def push_to_movie(country, info):
    global movies_list
    for index in movies_list:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    movies_list.append(tmp)
    return True


def check_type(link):
    link = link.split("/")
    if "series" in link:
        return "series"
    elif "movie" in link:
        return "movie"
    else:
        return "channel"
    





pass

def get_objects(myList, type):
    if len(myList) == 0:
        return None
    objects = []
    for i in myList:
        tmp = [i[0], []]
        for j in i[1]:
            if type == 'channels':
                object = Channel(j)
            elif type == 'movies':
                object = Movie(j)
            elif type == 'series':
                object = Series(j)
            tmp[1].append(object)
        objects.append(tmp)
    return objects


## parse movies 


series_cache_list = []
movies_cache_list = []
channels_cache_list = []

def get_series():
    global series_cache_list
    if len( series_cache_list ) > 0:
        return series_cache_list
    series_cache_list = get_objects(series_list, 'series')
    return series_cache_list

def get_channels():
    global channels_cache_list
    if len( channels_cache_list ) > 0:
        return series_cache_list
    channels_cache_list = get_objects(channels_list, 'channels')
    return channels_cache_list

def get_movies():
    global movies_cache_list
    if len( movies_cache_list ) > 0:
        return movies_cache_list
    movies_cache_list = get_objects(movies_list, 'movies')
    return movies_cache_list

