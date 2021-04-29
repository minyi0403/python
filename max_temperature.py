temperature = [] #存放所有有效溫度
time = [] #存放所有時間
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,525604): #蒐集有效溫度及時間
  if data[i][1] != ('None') and data[i][1] != ('-999.0') and data[i][1] != ('-910.0') :
    t=data[i][0]
    T=float(data[i][1])
    time.append(t)
    temperature.append(T)
max_temperature = max(temperature) #最大溫度

for i in range(len(temperature)): #將最大溫度輸出螢幕
  if temperature[i] == max_temperature:
    print(time[i])
    print(str(temperature[i])+' °C')
