# use bs4 and requests to get the html content of the website       
import requests 
import time
import sys
from datetime import datetime
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *

# requests the website 
url = "https://tixcraft.com/activity/game/23_caodong"
# refresh flag
not_available = True

ts = []

def get_ticket_status():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tr = soup.findAll("tr", class_="gridc fcTxt")
    for row in tr:
        cols = row.find_all("td")
        fourth_col_div = cols[3].find("div")
        if fourth_col_div:
            fourth_col_div_text = fourth_col_div.get_text(strip=True)
            if fourth_col_div_text != 'No tickets available':
                ts.append(cols[0].get_text(strip=True)+"," +cols[2].get_text(strip=True)+ "," +'釋票中')
            print(cols[0].get_text(strip=True) + "," + cols[2].get_text(strip=True)+","+fourth_col_div_text)

def has_ticket_alarm(self, ts: list) -> None:
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        Form.setWindowFlags(Qt.WindowStaysOnTopHint)
        Form.setWindowTitle('ticket')

        # 設置窗口大小
        Form.resize(500, 400)
        scroll_area = QtWidgets.QScrollArea(Form)
        scroll_area.setGeometry(0, 0, Form.width(), Form.height())  # 設置滾動區域的大小
        scroll_area.setWidgetResizable(True)
        label = QtWidgets.QLabel(scroll_area)
        label.setText(f''.join(ts))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        label.setFont(font)

        scroll_area.setWidget(label)
        scroll_area.show()
        Form.show()
        sys.exit(app.exec_())

 

while not_available:
    print("The current time is", datetime.now().strftime("%H:%M:%S"))
    get_ticket_status()
    
    if ts:
        not_available = False
        has_ticket_alarm(ts)
        
    time.sleep(5)
    