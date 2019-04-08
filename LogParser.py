from file_titles import titles
import os
import re


class LogParser:
    def __init__(self, file_name, file_format):
        self.file_name = file_name
        self.file_format = titles[file_format]['log_format']
        self.rex =  titles[file_format]['regex'][0]
        self.Read_file(self.file_name)


    def Read_file(self,file_name):
        try:
            f = open(self.file_name, "r")
            i = 0
            for line in f:
                i+=1
                print(re.findall(self.rex, line))
                if i==5:
                    break

        except Exception as e:
            print(e)


    def display(self):
        print("self.rex  : ", self.rex)
        print("self.format  : ", self.file_format)

