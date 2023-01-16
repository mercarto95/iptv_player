
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
        x = -1
        while len( line[x] ) < 40:
            x -= 1
        info = line[-1].split("\r")
        now = False
        link = ""
        length = []
        for i in info:
            length.append( len(i) )
        index = length.index( max(length) )
        try:
            index_http = info[index].index('http')
            link = info[index][index_http:]
        except:
            link = ""
        try:
            index = link.index('\\')
            link = link[:index]
        except:
            pass
        try:
            index = link.index('\n')
            link = link[:index]
        except:
            pass

        return link

#movie = Movie(x)
pass
