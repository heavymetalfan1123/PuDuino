from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import pyqtgraph as pg
serial = QSerialPort()
serial.setBaudRate(9600)
portlist = [] 
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portlist.append(port.portName())

listX = [i for i in range(100)]
listY = [0 for i in range(100)]
listY_2 = [0 for i in range(100)]
def openPort():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)
    #onRead()
    

def sendText():
    txs = ''
    txs += ui.textF.displayText()
    
    serial.write(txs.encode())
    

def closePort():
    serial.close()
def onRead():
    rx = serial.readLine()
    rx = str(rx,"utf-8").strip()
    rx = rx.split(",")
    global listX
    global listY
    global listY_2
    listY = listY[1:]
    listY_2 = listY_2[1:]
    listY.append(int(rx[0]))
    listY_2.append(int(rx[1]))
    #print(rx)
    ui.graph.clear()
    ui.graph.plot(listX, listY)
    ui.graph_2.clear()
    ui.graph_2.plot(listX, listY_2)


serial.readyRead.connect(onRead)

app =  QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Checker of life ")
ui.comL.addItems(portlist)


ui.comL.currentIndexChanged.connect(ui.comL.clear)
ui.openB.clicked.connect(openPort)
ui.closeB.clicked.connect(closePort)
ui.sendB.clicked.connect(sendText)
#onRead()
# data = data.append(onRead())
# pg.plot(data)

ui.show()
app.exec()
