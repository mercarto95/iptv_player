
class Account:
    def __init__(self, tv_name=None, username=None, password=None, server=None) -> None:
        if tv_name == username == password == server == None:
            self.accounts_list = []
            return None
        else:
            self.name = tv_name 
            self.username = username
            self.password = password
            self.server = server 
            if self.write_account_to_database():
                self.request_file_from_server()
        
    def read_accounts_from_database(self):
        """
        Read accounts file. Data gonna be converted from bin to string
        """
        try:
            f = open("./data/.accounts.bi", "r")
            lines = f.readlines()
            for line in lines:
                print(line)
            self.accounts_list = lines
            return lines
        except:
            print("Error while trying to read accounts file")
            return False
    
    def confirm_existing_account(self, name):
        for line in self.accounts_list:
            x = line.split(", ")
            if name in x:
                self.name = line[0]
                self.username = line[1]
                self.password = line[2]
                self.server = line[3]
                return True 
        return False
    

    
    def write_account_to_database(self):
        """
        Binary file. Data gonna be converted to binary.
        """
        try:
            f = open('./data/.accounts.bi', 'a')
            txt = f"{self.name}, {self.username}, {self.password}, {self.server}\n"
            f.write(txt)
            f.close()
            return True
        except:
            print("Error while opening/writing to the file")
            return False
    
    def binary_to_string(self, binary_data):
        def BinaryToDecimal(binary):
            binary1 = binary
            decimal, i, n = 0, 0, 0
            while(binary != 0):
                dec = binary % 10
                decimal = decimal + dec * pow(2, i)
                binary = binary//10
                i += 1
            return (decimal)
        str_data =' '
        for i in range(0, len(binary_data), 7):
            temp_data = int(binary_data[i:i + 7])
            decimal_data = BinaryToDecimal(temp_data)
            str_data = str_data + chr(decimal_data)
        return str_data
    
    def string_to_binary(string):
        bin = "".join(f"{ord(i):08b}" for i in string)
        return bin

    def request_file_from_server(self):
        pass


#a1 = Account("rodri_tv", "username1" , "password1", "http://seiewe.com")
pass