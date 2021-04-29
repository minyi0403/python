import matplotlib.pyplot as plt  # 導入python視覺畫會圖庫
S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,S11,S12 = [],[],[],[],[],[],[],[],[],[],[],[] # 2019一月到十二有效風速資料(非('None')或('-999.0'))
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,44644):  #蒐集2019一月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S1.append(S)
Janurary_windspeed = 0  #計算一月月均風速取到小數點後一位
for j in range(len(S1)):
    Janurary_windspeed += S1[j]  
Janurary_windspeed_mean = Janurary_windspeed/len(S1)
Janurary_windspeed_mean = round(Janurary_windspeed_mean,1)

for i in range(44644,84964):  #蒐集2019二月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S2.append(S)
Feburary_windspeed=0  #計算二月月均風速取到小數點後一位
for j in range(len(S2)):
    Feburary_windspeed += S2[j]  
Feburary_windspeed_mean = Feburary_windspeed/len(S2)
Feburary_windspeed_mean = round(Feburary_windspeed_mean,1)

for i in range(84964,129604):  #蒐集2019三月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S3.append(S)
March_windspeed = 0  #計算三月月均風速取到小數點後一位
for j in range(len(S3)):
    March_windspeed += S3[j]  
March_windspeed_mean = March_windspeed/len(S3)
March_windspeed_mean = round(March_windspeed_mean,1)

for i in range(129604,172804):  #蒐集2019四月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S4.append(S)
April_windspeed = 0  #計算四月月均風速取到小數點後一位
for j in range(len(S4)):
    April_windspeed+= S4[j]  
April_windspeed_mean = April_windspeed/len(S4)
April_windspeed_mean = round(April_windspeed_mean,1)

for i in range(172804,217444):  #蒐集2019五月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S5.append(S)
May_windspeed = 0  #計算五月月均風速取到小數點後一位
for j in range(len(S5)):
    May_windspeed += S5[j]  
May_windspeed_mean = May_windspeed/len(S5)
May_windspeed_mean = round(May_windspeed_mean,1)

for i in range(217444,260644):  #蒐集2019六月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S6.append(S)
June_windspeed = 0  #計算六月月均風速取到小數點後一位
for j in range(len(S6)):
    June_windspeed += S6[j]  
June_windspeed_mean = June_windspeed/len(S6)
June_windspeed_mean = round(June_windspeed_mean,1)

for i in range(260644,305284):  #蒐集2019七月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S7.append(S)
July_windspeed = 0  #計算七月月均風速取到小數點後一位
for j in range(len(S7)):
    July_windspeed += S7[j]  
July_windspeed_mean = July_windspeed/len(S7)
July_windspeed_mean = round(July_windspeed_mean,1)

for i in range(305284,349924):  #蒐集2019八月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S8.append(S)
Auguest_windspeed = 0  #計算八月月均風速取到小數點後一位
for j in range(len(S8)):
    Auguest_windspeed += S8[j]  
Auguest_windspeed_mean = Auguest_windspeed/len(S8)
Auguest_windspeed_mean = round(Auguest_windspeed_mean,1)

for i in range(349924,393124):  #蒐集2019九月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S9.append(S)
September_windspeed = 0  #計算九月月均風速取到小數點後一位
for j in range(len(S9)):
    September_windspeed += S9[j]  
September_windspeed_mean = September_windspeed/len(S9)
September_temperature_mean = round(September_windspeed_mean,1)

for i in range(393124,437764):  #蒐集2019十月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S10.append(S)
October_windspeed = 0  #計算十月月均風速取到小數點後一位
for j in range(len(S10)):
    October_windspeed += S10[j]  
October_windspeed_mean = October_windspeed/len(S10)
October_windspeed_mean = round(October_windspeed_mean,1)

for i in range(437764,480964):  #蒐集2019十一月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S11.append(S)
November_windspeed = 0  #計算十一月月均風速取到小數點後一位
for j in range(len(S11)):
    November_windspeed += S11[j]  
November_windspeed_mean = November_windspeed/len(S11)
November_windspeed_mean = round(November_windspeed_mean,1)

for i in range(480964,525604):  #蒐集2019十二月有效風速資料
  if data[i][5] != ('None') and data[i][5] != ('-999.0') :
    S = float(data[i][5])
    S12.append(S)
December_windspeed = 0  #計算十二月月均風速取到小數點後一位
for j in range(len(S12)):
    December_windspeed += S12[j]  
December_windspeed_mean = December_windspeed/len(S12)
December_windspeed_mean = round(December_windspeed_mean,1)

#繪製2019月均溫折線圖
y = [Janurary_windspeed_mean,Feburary_windspeed_mean,March_windspeed_mean,April_windspeed_mean,May_windspeed_mean,June_windspeed_mean,July_windspeed_mean,Auguest_windspeed_mean,September_temperature_mean,October_windspeed_mean,November_windspeed_mean,December_windspeed_mean]
x = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
plt.plot(x,y,'y-..')
plt.xlabel('Month',fontsize = 12)
plt.ylabel('Monthly average windspeed (m/s)',fontsize = 12)
for a,b in zip(x,y):
  plt.text(a,b,b, ha ='center', va= 'bottom',fontsize = 8)
plt.title('2019')
plt.show()