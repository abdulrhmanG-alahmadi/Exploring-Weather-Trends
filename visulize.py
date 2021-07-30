'''
this code was made by Abdulrhman Alahmadi and runs in linear time O(n)
please if you have any suggestions to make it more efficient share them with me
'''
import pandas as pd
import matplotlib.pyplot as plt

# getting csv files
globalData = pd.read_csv("C:\\Users\\alahm\\Desktop\\Data Analyst\\Global_data.csv")
makkahData = pd.read_csv("C:\\Users\\alahm\\Desktop\\Data Analyst\\x.csv")


# making the avrage to a moving avrage
globalData['avg_temp'] = globalData['avg_temp'].rolling(window=20).mean()
makkahData['avg_temp'] = makkahData['avg_temp'].rolling(window=20).mean()


# creating the plot

## making thicker lines in the graph
for i in range(10):
    plt.plot(makkahData['year'], makkahData['avg_temp'],color= 'gold')
    plt.plot(globalData['year'],globalData['avg_temp'],color= 'darkorange')
## one final ittretion with labels added    
plt.plot(makkahData['year'],makkahData['avg_temp'],color= 'gold',label='Makkah temperature')
plt.plot(globalData['year'],globalData['avg_temp'],color= 'darkorange',label='Global temperature')

##creating the title and labels while custmizing it as i see fit
plt.title('Temperature trends for the past 200 years',size=20, fontweight='bold', fontname='Helvetica')
plt.xlabel('Year',fontweight='bold', fontname='Helvetica')
plt.legend(shadow=True,loc='upper left')
plt.ylabel('Temperature (°C)',fontweight='bold',fontname='Helvetica')

# printing the final result
plt.show()


