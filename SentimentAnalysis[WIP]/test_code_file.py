import re

data = ["10/31/19, 9:43 PM - h_Achal Sharma: Jaskirat discord pe add kar sabko",
        "10/31/19, 9:43 PM - h_JizzyD: Ruk gimme 10",
        "10/31/19, 9:43 PM - h_Deepanshu: I don't have discord ",
        "Jab xbox live pe bhi connect kar sakte ho",
        "Mujhe username se nahi mil rahe tum origin pe",
        "10/31/19, 9:51 PM - Kakarot: tujhe nahi bheji.. kya id/username ?",
        "10/31/19, 9:51 PM - Kakarot: discord nahi hai",
        "10/31/19, 9:51 PM - h_JizzyD: Toh daal na bhai",
        "10/31/19, 9:51 PM - h_Deepanshu: Haan toh sahi daala hai tune ",
        "Meri email id ek baar daalke dekh" ]

finalList = list()

for i in range(len(data)):
                s = data[i]
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
                    Message = finalList[-1][3]
                    Chat = Message.join([" ", s])
                    finalList[-1][3] = Chat
                    
                    
gif = dict()
for i in range(4):
    gif[i] = i*i
    
