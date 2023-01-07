import os

f = open("./data/data.bi", "rb")

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
                countries.append(buffer)
            recognized_group_title = False 
            push_the_line(buffer, line)
        if word == " group-title=":
            #buffer += word
            recognized_group_title = True



pass


