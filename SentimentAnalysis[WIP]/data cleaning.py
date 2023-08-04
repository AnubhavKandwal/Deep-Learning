#phase 1 imports
import re
import csv
import win_unicode_console
win_unicode_console.enable()


#PHASE 1: Creating class that creates csv file based on whatsapp chat
'''
Handle the text file as source and break each message for data analysis - by saving it in a csv format.
Message broken into 5 parts:
            1. date
            2. time
            3. sender
            4. msg
'''      
class sourceData:
    
    #intialize the file
    def __init__(self,filename):
        self.filename = filename
    
    #create a list of the dataset
    def createList(self, num):
        file = open(self.filename,'r',encoding=('utf-8')) 
        chat = file.readlines()
                
        finalList = list()
        
        try:
            num = int(num)
        except:
            type(num) == str 
        
        if (type(num) == int):
            for i in range(num):
                s = chat[i]
                if re.search(r"^[0-9][0-9]/[0-9][0-9]/[0-9][0-9]", s):
                    time = s[s.find(','):s.find('-', s.find(','))]
                    date = s[0:s.find(',')]
                    Sender = s[s.find('-'):s.find(':',s.find('-'))]
                    Message = s[s.find(':',s.find('-')):]
                    
                    temp_list = list()
                    temp_list.append(date)
                    temp_list.append(time)
                    temp_list.append(Sender)
                    temp_list.append(Message)
                    
                    finalList.append(temp_list)
                
                else:
                    Msg = finalList[-1][3]
                    Cht = Msg.join([" ", s])
                    finalList[-1][3] = Cht
        else:
            for i in range(len(chat)):
                s = chat[i]
                if re.search(r"^[0-9][0-9]/[0-9][0-9]/[0-9][0-9]", s):
                    time = s[s.find(','):s.find('-', s.find(','))]
                    date = s[0:s.find(',')]
                    Sender = s[s.find('-'):s.find(':',s.find('-'))]
                    Message = s[s.find(':',s.find('-')):]
                    
                    temp_list = list()
                    temp_list.append(date)
                    temp_list.append(time)
                    temp_list.append(Sender)
                    temp_list.append(Message)
                    
                    finalList.append(temp_list)
                
                else:
                    Msg = finalList[-1][3]
                    Cht = Msg.join([" ", s])
                    finalList[-1][3] = Cht
        
        return finalList
    
    #creates an csv for the list generated
    def createDataset(self, lists):
            
        with open('Chat.csv','w', encoding=('utf-16')) as f:
            writer = csv.writer(f)
            writer.writerow(['Date','Time', 'Sender', 'Message'])
            writer.writerows(lists)
        print("'Chat.csv' successfully created.")
            
    #prints basic information about the files
    def fileInfo(self):
        
        print("File name: {0}".format(self.filename))
        print("Total messages: {0}".format(len(self.createList('default'))))


def main():
    
    print('File that needs to be opened:', end = ' ')
    filename = 'E:\\programming\\Project\\NLP\\spam_data\\WhatsApp Chat with XoN.txt'
    source = sourceData(filename)
    
    source.fileInfo()
    print('How many lines: (Type "All" for complete file)', end = ' ')
    num = input()
    value = source.createList(num)
    print(value)
    source.createDataset(value)


if __name__ == "__main__":
    main()
    
    
    