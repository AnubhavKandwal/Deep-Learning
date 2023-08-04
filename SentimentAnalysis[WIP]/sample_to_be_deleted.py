import re
sample = ['4/18/20, 2:03 AM - Kakarot: cuz tbh i will too in a while  . max 2:30', '4/18/20, 2:03 AM - Bublasaur: what up']

fl = list()

for i in range(len(sample)):

    s = sample[i]    
    time = s[s.find(','):s.find('-', s.find(','))]
    date = s[0:s.find(',')]
    Sender = s[s.find('-'):s.find(':',s.find('-'))]
    Message = s[s.find(':',s.find('-')):]
    
    temp_list = list()
    temp_list.append(date)
    temp_list.append(time)
    temp_list.append(Sender)
    temp_list.append(Message)

    fl.append(temp_list)
    
print(fl)