import matplotlib.pyplot as plt  # 導入python視覺畫會圖庫
T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12 = [],[],[],[],[],[],[],[],[],[],[],[] # 2019一月到十二有效溫度資料(非('None')或('-999.0'))
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,44644):  #蒐集2019一月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T1.append(T)
Janurary_temperature = 0  #計算一月月均溫取到小數點後一位
for j in range(len(T1)):
    Janurary_temperature +=T1[j]  
Janurary_temperature_mean = Janurary_temperature/len(T1)
Janurary_temperature_mean = round(Janurary_temperature_mean,1)

for i in range(44644,84964):  #蒐集2019二月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T2.append(T)
Feburary_temperature = 0  #計算二月月均溫取到小數點後一位
for j in range(len(T2)):
    Feburary_temperature += T2[j]  
Feburary_temperature_mean = Feburary_temperature/len(T2)
Feburary_temperature_mean = round(Feburary_temperature_mean,1)

for i in range(84964,129604):  #蒐集2019三月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T3.append(T)
March_temperature = 0  #計算三月月均溫取到小數點後一位
for j in range(len(T3)):
    March_temperature += T3[j]  
March_temperature_mean = March_temperature/len(T3)
March_temperature_mean = round(March_temperature_mean,1)

for i in range(129604,172804):  #蒐集2019四月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T4.append(T)
April_temperature = 0  #計算四月月均溫取到小數點後一位
for j in range(len(T4)):
    April_temperature += T4[j]  
April_temperature_mean = April_temperature/len(T4)
April_temperature_mean = round(April_temperature_mean,1)

for i in range(172804,217444):  #蒐集2019五月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T5.append(T)
May_temperature = 0  #計算五月月均溫取到小數點後一位
for j in range(len(T5)):
    May_temperature += T5[j]  
May_temperature_mean = May_temperature/len(T5)
May_temperature_mean = round(May_temperature_mean,1)

for i in range(217444,260644):  #蒐集2019六月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T6.append(T)
June_temperature = 0  #計算六月月均溫取到小數點後一位
for j in range(len(T6)):
    June_temperature += T6[j]  
June_temperature_mean = June_temperature/len(T6)
June_temperature_mean = round(June_temperature_mean,1)

for i in range(260644,305284):  #蒐集2019七月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T7.append(T)
July_temperature = 0  #計算七月月均溫取到小數點後一位
for j in range(len(T7)):
    July_temperature += T7[j]  
July_temperature_mean = July_temperature/len(T7)
July_temperature_mean = round(July_temperature_mean,1)

for i in range(305284,349924):  #蒐集2019八月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T8.append(T)
Auguest_temperature = 0  #計算八月月均溫取到小數點後一位
for j in range(len(T8)):
    Auguest_temperature += T8[j]  
Auguest_temperature_mean = Auguest_temperature/len(T8)
Auguest_temperature_mean = round(Auguest_temperature_mean,1)

for i in range(349924,393124):  #蒐集2019九月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T9.append(T)
September_temperature = 0  #計算九月月均溫取到小數點後一位
for j in range(len(T9)):
    September_temperature += T9[j]  
September_temperature_mean = September_temperature/len(T9)
September_temperature_mean = round(September_temperature_mean,1)

for i in range(393124,437764):  #蒐集2019十月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T10.append(T)
October_temperature = 0  #計算十月月均溫取到小數點後一位
for j in range(len(T10)):
    October_temperature += T10[j]  
October_temperature_mean = October_temperature/len(T10)
October_temperature_mean = round(October_temperature_mean,1)

for i in range(437764,480964):  #蒐集2019十一月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1])
    T11.append(T)
November_temperature = 0  #計算十一月月均溫取到小數點後一位
for j in range(len(T11)):
    November_temperature += T11[j]  
November_temperature_mean = November_temperature/len(T11)
November_temperature_mean = round(November_temperature_mean,1)

for i in range(480964,525604):  #蒐集2019十二月有效溫度資料
  if data[i][1] != ('None') and data[i][1] != ('-999.0') :
    T = float(data[i][1]) 
    T12.append(T)
December_temperature = 0  #計算十二月月均溫取到小數點後一位
for j in range(len(T12)):
    December_temperature += T12[j]  
December_temperature_mean = December_temperature/len(T12)
December_temperature_mean = round(December_temperature_mean,1)

#繪製2019月均溫折線圖
y = [Janurary_temperature_mean,Feburary_temperature_mean,March_temperature_mean,April_temperature_mean,May_temperature_mean,June_temperature_mean,July_temperature_mean,Auguest_temperature_mean,September_temperature_mean,October_temperature_mean,November_temperature_mean,December_temperature_mean]
x = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
plt.plot(x,y,'r-..')
plt.xlabel('Month',fontsize = 12)
plt.ylabel('Monthly average temperature (°C)',fontsize = 12)
for a,b in zip(x,y):
  plt.text(a,b,b, ha ='center', va= 'bottom',fontsize = 8)
plt.title('2019')
plt.show()