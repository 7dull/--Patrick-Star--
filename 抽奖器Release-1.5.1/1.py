"""
By 7dull_
############################
#--------By 7dull_---------#
############################
"""
import os
import random
import threading
import time
import webbrowser

from PySide2 import QtCore, QtGui
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

'''
不是全部都有用
'''
if not os.path.exists("./files/list"):
    os.makedirs("./files/list")  # 防止文件夹被删
with open("./files/list/num.r", "w") as f:
    f.write("1")  # 覆盖num
app = QApplication([])
ui = QUiLoader().load('./files/ui.ui')  # 加载ui文件
ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 删除头栏
icon_1 = QtGui.QIcon()
icon_1.addPixmap(QtGui.QPixmap("./files/image/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
icon_2 = QtGui.QIcon()
icon_2.addPixmap(QtGui.QPixmap("./files/image/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
ui.bquit.setIcon(icon_1)
ui.back.setIcon(icon_2)
'''
读取UI文件修改部分设置并设置图标
'''
ui.show_2.close()
ui.back.close()
'''
以上为伪弹窗,需要时在启动后关闭,被刺激时显示
现在是先关闭,等待被显示
'''


# 函数区↓
def down():
    ui.show_2.close()
    ui.back.close()
    '''伪弹窗的关闭实现'''


def bquit():
    ui.close()
    '''软件的关闭实现'''


def website():
    url = "https://github.com/7dull/--Patrick-Star--"
    webbrowser.open(url)
    '''前往Github(开源)实现'''


def b_count():
    with open("./files/list/num.r", "r") as F:
        num = F.read()
    num = int(num)
    num -= 1
    ui.show_2.show()
    ui.show_2.raise_()
    ui.back.show()
    ui.back.raise_()
    ui.show_2.setText("一共{}人".format(num))
    '''"统计"实现'''


def b_add():
    text = ui.input.text()
    ui.input.clear()
    if text == "":
        pass
    elif text == " ":
        pass
    elif text == "  ":
        pass
    # ↑防空格
    else:
        with open("./files/list/num.r", "r") as F:
            num = F.read()
        ui.list.addItem("{}: ".format(num) + text)
        with open("./files/list/num.r", "r") as F:
            num = F.read()
        num = int(num)
        with open("./files/list/{}.list".format(num), "w") as F:
            F.write(text)
        num += 1
        num = str(num)
        with open("./files/list/num.r", "w") as F:
            F.write(num)
    '''"添加"实现'''


def b_cancel():
    item = ui.list.currentItem()
    ui.list.takeItem(ui.list.row(item))
    print(item)
    with open("./files/list/num.r", "r") as F:
        num = F.read()
    num = int(num)
    num -= 1
    num = str(num)
    with open("./files/list/num.r", "w") as F:
        F.write(num)
    '''"删出"实现'''


def b_clean():
    ui.input.clear()
    with open("./files/list/num.r", "w") as F:
        F.write("1")
    ui.list.clear()
    '''"清空"实现'''


def b_roll():
    with open("./files/list/num.r", "r") as F:
        num = F.read()
    num = int(num)
    num -= 1
    ui.show_2.show()
    ui.show_2.raise_()
    ui.back.show()
    ui.back.raise_()  # 伪弹窗显示
    ui.show_2.setText("无参加人员！")
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText(winner)
    roll()


# 函数区↑
ui.bquit.clicked.connect(bquit)  # 关闭软件
ui.bwebsite.clicked.connect(website)  # Github跳转
ui.add.clicked.connect(b_add)  # "添加"
ui.clean.clicked.connect(b_clean)  # "清空"
ui.cancel.clicked.connect(b_cancel)  # "删除"
ui.run.clicked.connect(b_roll)  # "-抽奖—"
ui.back.clicked.connect(down)  # 关闭弹窗
ui.count.clicked.connect(b_count)  # "统计"
'''
绑定事件函数
全部可以在上面函数区被找到并修改(自定义)
'''


def am():
    with open("./files/list/num.r", "r") as F:
        num = F.read()
    num = int(num)
    num -= 1
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("滚动中:\n" + winner)
    time.sleep(0.2)
    winner_num = random.randint(1, num)
    with open("./files/list/{}.list".format(winner_num), "r") as F:
        winner = F.read()
    ui.show_2.setText("恭喜:\n" + winner)
    time.sleep(0.5)


def roll():
    t1 = threading.Thread(target=am, )
    t1.start()


ui.show()  # 窗口显示
app.exec_()  # 窗口循环
