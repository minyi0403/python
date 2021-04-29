import matplotlib.pyplot as plt  # 導入python視覺畫會圖庫
P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12 = [],[],[],[],[],[],[],[],[],[],[],[] # 2019一月到十二有效壓力資料(非('None')或('-999.0'))
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,44644):  #蒐集2019一月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P1.append(P)
Janurary_pressure = 0  #計算一月壓力平均取到小數點後一位
for j in range(len(P1)):
    Janurary_pressure += P1[j]  
Janurary_pressure_mean = Janurary_pressure/len(P1)
Janurary_pressure_mean = round(Janurary_pressure_mean,1)

for i in range(44644,84964):  #蒐集2019二月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P2.append(P)
Feburary_pressure = 0  #計算二月壓力平均取到小數點後一位
for j in range(len(P2)):
    Feburary_pressure += P2[j]  
Feburary_pressure_mean = Feburary_pressure/len(P2)
Feburary_pressure_mean = round(Feburary_pressure_mean,1)

for i in range(84964,129604):  #蒐集2019三月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P3.append(P)
March_pressure = 0  #計算三月壓力平均取到小數點後一位
for j in range(len(P3)):
    March_pressure += P3[j]  
March_pressure_mean = March_pressure/len(P3)
March_pressure_mean = round(March_pressure_mean,1)

for i in range(129604,172804):  #蒐集2019四月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P4.append(P)
April_pressure = 0  #計算四月壓力平均取到小數點後一位
for j in range(len(P4)):
    April_pressure += P4[j]  
April_pressure_mean = April_pressure/len(P4)
April_pressure_mean = round(April_pressure_mean,1)

for i in range(172804,217444):  #蒐集2019五月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P=float(data[i][3])
    P5.append(P)
May_pressure = 0  #計算五月壓力平均取到小數點後一位
for j in range(len(P5)):
    May_pressure += P5[j]  
May_pressure_mean = May_pressure/len(P5)
May_pressure_mean = round(May_pressure_mean,1)

for i in range(217444,260644):  #蒐集2019六月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P6.append(P)
June_pressure = 0  #計算六月壓力平均取到小數點後一位
for j in range(len(P6)):
    June_pressure += P6[j]  
June_pressure_mean = June_pressure/len(P6)
June_pressure_mean = round(June_pressure_mean,1)

for i in range(260644,305284):  #蒐集2019七月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P7.append(P)
July_pressure = 0  #計算七月壓力平均取到小數點後一位
for j in range(len(P7)):
    July_pressure += P7[j]  
July_pressure_mean = July_pressure/len(P7)
July_pressure_mean = round(July_pressure_mean,1)

for i in range(305284,349924):  #蒐集2019八月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P8.append(P)
Auguest_pressure = 0  #計算八月壓力平均取到小數點後一位
for j in range(len(P8)):
    Auguest_pressure += P8[j]  
Auguest_pressure_mean = Auguest_pressure/len(P8)
Auguest_pressure_mean = round(Auguest_pressure_mean,1)

for i in range(349924,393124):  #蒐集2019九月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P9.append(P)
September_pressure = 0  #計算九月壓力平均取到小數點後一位
for j in range(len(P9)):
    September_pressure += P9[j]  
September_pressure_mean = September_pressure/len(P9)
September_pressure_mean = round(September_pressure_mean,1)

for i in range(393124,437764):  #蒐集2019十月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P10.append(P)
October_pressure = 0  #計算十月壓力平均取到小數點後一位
for j in range(len(P10)):
    October_pressure += P10[j]  
October_pressure_mean = October_pressure/len(P10)
October_pressure_mean = round(October_pressure_mean,1)

for i in range(437764,480964):  #蒐集2019時十一月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P11.append(P)
November_pressure = 0  #計算十一月壓力平均取到小數點後一位
for j in range(len(P11)):
    November_pressure += P11[j]  
November_pressure_mean = November_pressure/len(P11)
November_pressure_mean = round(November_pressure_mean,1)

for i in range(480964,525604):  #蒐集2019十二月有效壓力資料
  if data[i][3] != ('None') and data[i][3] != ('-999.0') :
    P = float(data[i][3])
    P12.append(P)
December_pressure = 0  #計算十二月壓力平均取到小數點後一位
for j in range(len(P12)):
    December_pressure += P12[j]  
December_pressure_mean = December_pressure/len(P12)
December_pressure_mean = round(December_pressure_mean,1)
#繪製2019月均壓力折線圖
y = [Janurary_pressure_mean,Feburary_pressure_mean,March_pressure_mean,April_pressure_mean,May_pressure_mean,June_pressure_mean,July_pressure_mean,Auguest_pressure_mean,September_pressure_mean,October_pressure_mean,November_pressure_mean,December_pressure_mean]
x = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
plt.plot(x,y,'b-')
plt.xlabel('Month',fontsize= 12)
plt.ylabel('Monthly average pressure',fontsize = 12)
for a,b in zip(x,y):
  plt.text(a,b,b, ha ='center', va= 'bottom',fontsize = 8)
plt.title('2019')
plt.show()