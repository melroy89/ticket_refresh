# 本機執行建議先用虛擬環境
1.
```
  virtualenv ticket_env  #建立虛擬環境
  win: ticket_env\Scripts\activate   #進入虛擬環境
  macOS: source ./ticket_env/bin/activate
```
2.
```
 pip3 install -r requirements.txt
```

3.
```
 python3 main.py
```

4. 成功監票會顯示

```
The current time is 15:27:46
2023/05/24 (Wed.)  20:00,Legacy Taipei,No tickets available
2023/05/26 (Fri.)  20:00,Legacy Taipei,No tickets available
2023/05/28 (Sun.)  20:00,Legacy Taipei,No tickets available
2023/05/31 (Wed.)  20:00,Legacy Taichung,No tickets available
2023/06/02 (Fri.)  20:00,Legacy Taichung,No tickets available
2023/06/04 (Sun.)  20:00,Legacy Taichung,No tickets available
2023/06/07 (Wed.)  20:00,LIVE WAREHOUSE,No tickets available
2023/06/09 (Fri.)  20:00,LIVE WAREHOUSE,No tickets available
2023/06/11 (Sun.)  20:00,LIVE WAREHOUSE,No tickets available
```

