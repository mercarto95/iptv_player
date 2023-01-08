import os

f = open("../data/test.bi", "rb")

file = f.read()
if len(file) == 0:
    print("File is empty")
    os._exit(100)
f.close()

pass


# each line beginning with "#EXTINF:-1 "
text = file.decode()
lines = text.split("#EXTINF:-1 ")
item = lines[2]

memory = []
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

def handle_country(param):
    if param in countries:
        return False
    return True



def push_the_line(country, info):
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
    for index in channels_list:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    channels_list.append(tmp)
    return True

def push_to_series(country, info):
    for index in series_list:
        if index[0] == country:
            index[1].append(info)
            return True
    # then new category, push it to the memory
    tmp = [country, [info]]
    series_list.append(tmp)
    return True

def push_to_movie(country, info):
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
    

countries = []
tot = []
recognized_group_title = False
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





pass



## parse movies 

