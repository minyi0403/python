import matplotlib.pyplot as plt  # 導入python視覺畫會圖庫
H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12 = [],[],[],[],[],[],[],[],[],[],[],[] # 2019一月到十二有效濕度資料(非('None')或('-999.0'))
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,44644):  #蒐集2019一月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H1.append(H)
Janurary_humidity = 0  #計算一月濕度平均取到小數點後一位
for j in range(len(H1)):
    Janurary_humidity += H1[j]  
Janurary_humidity_mean = Janurary_humidity/len(H1)
Janurary_humidity_mean = round(Janurary_humidity_mean,1)

for i in range(44644,84964):  #蒐集2019二月有效濕度資料
  if data[i][2] != ('None') and data[i][2]!=('-999.0') :
    H = float(data[i][2])
    H2.append(H)
Feburary_humidity = 0  #計算二月濕度平均取到小數點後一位
for j in range(len(H2)):
    Feburary_humidity += H2[j]  
Feburary_humidity_mean = Feburary_humidity/len(H2)
Feburary_humidity_mean = round(Feburary_humidity_mean,1)

for i in range(84964,129604):  #蒐集2019三月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H3.append(H)
March_humidity = 0  #計算三月濕度平均取到小數點後一位
for j in range(len(H3)):
    March_humidity += H3[j]  
March_humidity_mean = March_humidity/len(H3)
March_humidity_mean = round(March_humidity_mean,1)

for i in range(129604,172804):  #蒐集2019四月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H4.append(H)
April_humidity = 0  #計算四月濕度平均取到小數點後一位
for j in range(len(H4)):
    April_humidity += H4[j]  
April_humidity_mean = April_humidity/len(H4)
April_humidity_mean = round(April_humidity_mean,1)

for i in range(172804,217444):  #蒐集2019五月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H5.append(H)
May_humidity = 0  #計算五月濕度平均取到小數點後一位
for j in range(len(H5)):
    May_humidity += H5[j]  
May_humidity_mean = May_humidity/len(H5)
May_humidity_mean = round(May_humidity_mean,1)

for i in range(217444,260644):  #蒐集2019六月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H6.append(H)
June_humidity = 0  #計算六月濕度平均取到小數點後一位
for j in range(len(H6)):
    June_humidity += H6[j]  
June_humidity_mean = June_humidity/len(H6)
June_humidity_mean = round(June_humidity_mean,1)

for i in range(260644,305284):  #蒐集2019七月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H7.append(H)
July_humidity = 0  #計算七月濕度平均取到小數點後一位
for j in range(len(H7)):
    July_humidity += H7[j]  
July_humidity_mean = July_humidity/len(H7)
July_humidity_mean = round(July_humidity_mean,1)

for i in range(305284,349924):  #蒐集2019八月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H8.append(H)
Auguest_humidity = 0  #計算八月濕度平均取到小數點後一位
for j in range(len(H8)):
    Auguest_humidity += H8[j]  
Auguest_humidity_mean = Auguest_humidity/len(H8)
Auguest_humidity_mean = round(Auguest_humidity_mean,1)

for i in range(349924,393124):  #蒐集2019九月有效濕度資料
  if data[i][2] != ('None') and data[i][2]!=('-999.0') :
    H = float(data[i][2])
    H9.append(H)
September_humidity = 0  #計算九月濕度平均取到小數點後一位
for j in range(len(H9)):
    September_humidity += H9[j]  
September_humidity_mean = September_humidity/len(H9)
September_humidity_mean = round(September_humidity_mean,1)

for i in range(393124,437764):  #蒐集2019十月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H10.append(H)
October_humidity = 0  #計算十月濕度平均取到小數點後一位
for j in range(len(H10)):
    October_humidity += H10[j]  
October_humidity_mean = October_humidity/len(H10)
October_humidity_mean = round(October_humidity_mean,1)

for i in range(437764,480964):  #蒐集2019時十一月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H11.append(H)
November_humidity = 0  #計算十一月濕度平均取到小數點後一位
for j in range(len(H11)):
    November_humidity += H11[j]  
November_humidity_mean = November_humidity/len(H11)
November_humidity_mean = round(November_humidity_mean,1)

for i in range(480964,525604):  #蒐集2019十二月有效濕度資料
  if data[i][2] != ('None') and data[i][2] != ('-999.0') :
    H = float(data[i][2])
    H12.append(H)
December_humidity = 0  #計算十二月濕度平均取到小數點後一位
for j in range(len(H12)):
    December_humidity += H12[j]  
December_humidity_mean = December_humidity/len(H12)
December_humidity_mean = round(December_humidity_mean,1)
#繪製2019月均濕度折線圖
y = [Janurary_humidity_mean,Feburary_humidity_mean,March_humidity_mean,April_humidity_mean,May_humidity_mean,June_humidity_mean,July_humidity_mean,Auguest_humidity_mean,September_humidity_mean,October_humidity_mean,November_humidity_mean,December_humidity_mean]
x = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
plt.plot(x,y,'g-+')
plt.xlabel('Month',fontsize= 12)
plt.ylabel('Monthly average humidity (%)',fontsize = 12)
for a,b in zip(x,y):
  plt.text(a,b,b, ha='center', va = 'bottom',fontsize = 8)
plt.title('2019')
plt.show()