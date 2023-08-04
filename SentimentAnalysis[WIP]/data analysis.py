#PHASE 2: Data cleaning phase - clean the known issues with the csv created
'''
The known issue with the csv are:
    1. '- ' symbol in the Sender column
    2. ': ' symbol in the message column
    3. Blank spaces in between each data entry - is it because of the \n ?? [Need investigation]
    4. Emoji usage is now blank text - ignore or add value?
    5. '<Media omitted>' messages to be handled properly - to be removed as data point ? [Reduces time series setup - replace as 'MediaSent'?]
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#cleaning the data
data = pd.read_csv('Chat.csv', encoding=('utf-16'))
data.drop('Time', axis = 1, inplace = True)
data['Sender'] = data['Sender'].str.lstrip('- ')
data['Message'] = data['Message'].str.lstrip(': ')

Messengers = data['Sender'].unique()
Messengers = np.delete(Messengers, [0,1,6,7])

plt.rcParams['figure.dpi'] = 720
plt.rcParams['font.size'] = '14'
plt.figure(figsize=(15,14))
plt.figure(title = 'XON')

#Chart utility
LineColor = '#9a44af'
Names = ['Deepanshu', 'Achal', 'Jaskirat' ,'Anubhav']
ColorScheme = ['#c60101','#09bbf2', '#09f2a4', '#abba0e']

#Pie plot
pieplot = data.groupby('Sender').count()
pieplot = pieplot.drop(pieplot.index[[1,2,3,5]])
Explosion = [0.01,0.01,0.01,0.01]

#Line plot
x_axis = data['Date'].unique()
y_axis = data.groupby('Date').count()

#Bar chart
gif = list()
for i in range(len(Messengers)):
    count = data[(data['Message'] == "<Media omitted>\r\n") & (data['Sender'] == Messengers[i])].count()
    gif.append(count[2])

wide = [0.6,0.6,0.6,0.6]


#Subplot-1
plt.subplot(2,2,1)
plt.pie(pieplot['Message'],colors = ColorScheme, explode=Explosion, labels = Names)
plt.title('Message Contribution', fontsize = 20)

#Subplot-2
plt.subplot(2,2,2)
plt.bar(Names, gif, wide, color = ColorScheme, edgecolor = 'black', animated = True)
plt.title('Media Sent', fontsize = 20)
for i in range(len(Messengers)):
    plt.text(i,8, gif[i], horizontalalignment='center')

#Subplot-3
plt.subplot(2,1,2)
plt.plot(x_axis, y_axis, color = LineColor)
plt.title('Message Trend', fontsize = 20)
plt.xticks(fontsize = 2, rotation= 90)

#plt.savefig('Dashboard.png', dpi = 480)