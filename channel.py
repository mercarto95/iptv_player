
class Channel:
    def __init__(self, line):
        self.parse_line(line)
        self.channel_id = self.parse_id(line)
        self.channel_name = self.parse_name(line)
        self.logo = self.pase_logo(line)
        self.group = self.parse_group(line)
        self.link = self.parse_link(line)
    
    def parse_line(self, line):
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
        info = line[-1].split("\\")
        length_list = []
        for i in info:
            length_list.append( len(i) )
        index = length_list.index( max(length_list) )
        link = info[index]
        link =info[1:]
        return link

        
