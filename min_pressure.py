pressure = [] #存放所有的有效氣壓值
time = [] #存放所有的時間
file_input = 'Data_2019.txt' # 中大測站2019整年資料的相對路徑
with open(file_input, 'r') as f:   # 開啟檔案
    data = f.readlines()      # 讀檔
    data = [i.strip("\n").strip('"').split(",") for i in data] # 讀取到的資料整理

for i in range(4,525604): #蒐集有效氣壓及時間
  if data[i][3] != ('None') and data[i][3]!=('-999.0') and data[i][3]!=('-910.0') :
    t=data[i][0]
    p=float(data[i][3])
    time.append(t)
    pressure.append(p)

min_pressure = min(pressure) #找到最小氣壓值

for i in range(len(pressure)): #將最小氣壓輸出螢幕
  if pressure[i] == min_pressure:
    print(time[i])
    print(str(pressure[i])+' hpa')
