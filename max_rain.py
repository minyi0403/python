rain = [] #存放每小時總雨量
time = [] #存放整點時間
rain_total = 0
count = 0
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(24*365): #蒐集整點時間
  time.append(data[4+60*i][0]) 

for j in range(4,525604): #蒐集每小時總雨量
      if data[j][6] != ('None') and data[j][6] != ('-999.0') and data[j][6] != ('-910.0') :
        data[j][6]=  float(data[j][6])
        rain_total += data[j][6]
        count += 1
      else:
        data[j][6] = 0  
        rain_total += data[j][6]
        count += 1 
      while count == 60:
        rain.append(rain_total)
        count = 0
        rain_total = 0

max_rain=max(rain) #最大雨量

for i in range(len(rain)):        #將最大雨量輸出螢幕
      if rain[i]==max_rain:
        print(time[i])
        print(str(rain[i])+'mm')



