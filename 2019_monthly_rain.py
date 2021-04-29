import matplotlib.pyplot as plt  # 導入python視覺畫會圖庫
R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12 = [],[],[],[],[],[],[],[],[],[],[],[] # 2019一月到十二有效雨量資料(非('None')或('-999.0'))
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",")for i in data] # 讀取到的資料整理

for i in range(4,44644):  #蒐集2019一月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R1.append(R)
Janurary_rain = 0  #計算一月總雨量取到小數點後一位
for j in range(len(R1)):
    Janurary_rain += R1[j]  
Janurary_rain = round(Janurary_rain,1)

for i in range(44644,84964):  #蒐集2019二月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R2.append(R)
Feburary_rain = 0  #計算二月總雨量取到小數點後一位
for j in range(len(R2)):
    Feburary_rain += R2[j]  
Feburary_rain = round(Feburary_rain,1)

for i in range(84964,129604):  #蒐集2019三月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R3.append(R)
March_rain = 0  #計算三月總雨量取到小數點後一位
for j in range(len(R3)):
    March_rain += R3[j]  
March_rain = round(March_rain,1)

for i in range(129604,172804):  #蒐集2019四月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R4.append(R)
April_rain = 0  #計算四月總雨量取到小數點後一位
for j in range(len(R4)):
    April_rain += R4[j]  
April_rain = round(April_rain,1)

for i in range(172804,217444):  #蒐集2019五月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R5.append(R)
May_rain = 0  #計算五月總雨量取到小數點後一位
for j in range(len(R5)):
    May_rain += R5[j]  
May_rain = round(May_rain,1)
 
for i in range(217444,260644):  #蒐集2019六月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R6.append(R)
June_rain = 0  #計算六月總雨量取到小數點後一位
for j in range(len(R6)):
    June_rain += R6[j]  
June_rain = round(June_rain,1)

for i in range(260644,305284):  #蒐集2019七月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R7.append(R)
July_rain = 0  #計算七月總雨量取到小數點後一位
for j in range(len(R7)):
    July_rain += R7[j]  
July_rain = round(July_rain,1)

for i in range(305284,349924):  #蒐集2019八月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R8.append(R)
Auguest_rain = 0  #計算八月總雨量取到小數點後一位
for j in range(len(R8)):
    Auguest_rain += R8[j]  
Auguest_rain = round(Auguest_rain,1)

for i in range(349924,393124):  #蒐集2019九月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R9.append(R)
September_rain = 0  #計算九月總雨量取到小數點後一位
for j in range(len(R9)):
    September_rain += R9[j]  
September_rain = round(September_rain,1)

for i in range(393124,437764):  #蒐集2019十月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R10.append(R)
October_rain = 0  #計算十月總雨量取到小數點後一位
for j in range(len(R10)):
    October_rain += R10[j]  
October_rain= round(October_rain,1)

for i in range(437764,480964):  #蒐集2019十一月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R11.append(R)
November_rain = 0  #計算十一月總雨量取到小數點後一位
for j in range(len(R11)):
    November_rain += R11[j]  
November_rain = round(November_rain,1)

for i in range(480964,525604):  #蒐集2019十二月有效雨量資料
  if data[i][6] != ('None') and data[i][6] != ('-999.0') :
    R = float(data[i][6])
    R12.append(R)
December_rain = 0  #計算十二月總雨量取到小數點後一位
for j in range(len(R12)):
    December_rain += R12[j]  
December_rain = round(December_rain,1)



#繪製2019總雨量長條圖
y = [Janurary_rain,Feburary_rain,March_rain,April_rain,May_rain,June_rain,July_rain,Auguest_rain,September_rain,October_rain,November_rain,December_rain]
x = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
fig = plt.figure()
plt.bar(x,y,label = 'Sum_Rain',color = 'blue',width = 0.5)
plt.ylabel('Rainfall(mm)')
for a,b in zip(x,y):
      plt.text(a,b,b, ha = 'center', va = 'bottom',fontsize = 8)
plt.title('2019')
plt.legend()
plt.show()
