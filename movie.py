
class Movie:
    def __init__(self, line):
        self.id = self.parse_id(line)
        self.name = self.parse_name(line)
        self.logo = self.parse_logo(line)
        self.group = self.parse_group(line)
        self.link = self.parse_link(line)
    
    def parse_group(self, line):
        x = line.split('"')
        return x[7]
    
    def parse_logo(self, line):
        x = line.split('"')
        return x[5]
    
    def parse_name(self, line):
        x = line.split('"')
        return x[3]
    
    def parse_id(self, line):
        x = line.split('"')
        return x[1]
    
    def parse_link(self, line):
        line = line.split(" ")
        info = line[-1].split("\r")
        now = False
        link = ""
        index = info[0].index('http')
        link = info[0][index:]
        try:
            index = link.index('\\')
            link = link[:index]
        except:
            print("channel, except (2)")

        return link

#movie = Movie(x)
pass
