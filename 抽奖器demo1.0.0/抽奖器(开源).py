
#designed by 7dull_

import telnetlib
import tkinter as tk
import tkinter.messagebox
import webbrowser
import random
import os

with open("./PatrickStar/num.PatrickStar","w") as f:
    f.write("0")#默认为0
#覆盖上次程序修改的num数值
with open("./PatrickStar/list.PatrickStar","w") as f:
    f.write("")
#覆盖上次程序修改的list

cnm=tk.Tk() #创建窗口变
cnm.title('--Patrick-Star--(直播间抽奖器)') #窗口命名
cnm.geometry('500x500') #窗口大小
cnm.resizable(0,0)#锁定窗口大小

a=tkinter.messagebox.askyesno(title = '--Patrick-Star--(直播间抽奖器)',message='是否支持派总？\n开发信息:by 7dull_')
#a为开发信息确认弹窗返回的数值
if a==True:
    pass#确认继续运行
else:
    tkinter.messagebox.showerror(title='--Patrick-Star--(直播间抽奖器)', message='不支持我自己退出了\nqwq')#告知
    quit()#否定自动退出

try:
    telnetlib.Telnet('119.3.238.64', port='{}'.format(80), timeout=20)#测试网络连接，为后续的开发准备
    #借用一下阿b的资源
except:
    network = 0
    tkinter.messagebox.showerror(title = '--Patrick-Star--(直播间抽奖器)',message='连接不到 服务器')#告知
else:
    network=1#无用

def wdnmd_a():#修复（刷新）函数
    tkinter.messagebox.showinfo(title='--Patrick-Star--(直播间抽奖器)', message='修复完成')
    with open("./PatrickStar/num.PatrickStar", "r") as f:
        num = f.read()
    num=int(num)#转化数据
    for sb in range(1,num+1):
        az.delete(sb)#有点bug
    with open("./PatrickStar/num.PatrickStar", "w") as f:
        f.write("0")
    for sb_b in range(1,num+1):
        sb_b_A="./PatrickStar/list/{}.PatrickStar".format(sb_b)
        os.remove(sb_b_A)


wdnmd = tk.Button(cnm, text="出了问题请点我(修复)", command=wdnmd_a,font=('微软雅黑', 8),bg="#FFFFFF")
#刷新一下
wdnmd.place(x=380,y=470)

def qwq_a():#链接跳转函数
    if network==0:#无网络连接
        tkinter.messagebox.showerror(title='--Patrick-Star--(直播间抽奖器)', message='连接不到 服务器')
    else:
        url="https://github.com/7dull/--Patrick-Star--"#github开源
        webbrowser.open(url)

qwq = tk.Button(cnm, text="前往查看源码(开源)", command=qwq_a,font=('微软雅黑', 8),bg="#FFFFFF")
#开源链接
qwq.place(x=270,y=470)

nmsl= tkinter.Entry(cnm, width=20, font=('Arial', 14))
nmsl.place(x=180,y=100)#输入框

awa = tk.Label(cnm, text='◈抽奖名单输入', font=('微软雅黑', 12), width=10, height=2)
awa.place(x=60,y=90)

def yyds_a():  # 读取文件
    with open("./PatrickStar/num.PatrickStar", "r") as f:  # 打开文件
        num = f.read()#读取num数值
    num=int(num)#转换num数值以便加减
    num+=1
    num=str(num)#转换num数值以便写入
    with open("./PatrickStar/num.PatrickStar", "w") as f:# 打开文件
        f.write(num)# 写入文件
    nmsl_a=nmsl.get()#获取输入框内容
    num = int(num)#转换num数值以便print
    az.insert(num, "{}.{}".format(num,nmsl_a))#向list添加get到的数值
    with open("./PatrickStar/list/{}.PatrickStar".format(num), "w") as f:# 打开文件
        f.write(nmsl_a)

yyds= tk.Button(cnm, text="确认添加", command=yyds_a,font=('微软雅黑', 8),bg="#FFFFFF")
yyds.place(x=350,y=130)#"确认添加按钮"

az = tkinter.Listbox(cnm)
az.pack(side=tkinter.LEFT, padx=5, pady=10)#创建列表变量

def delete():#删除列表选中内容函数
    index = az.curselection()#变量index=鼠标所选列表内容
    if len(index) == 0:#如果index为空
        return#返回
    az.delete(index)#删除index（鼠标所选）内容

wc= tk.Button(cnm, text="删除", command=delete,font=('微软雅黑', 8),bg="#FFFFFF")
wc.place(x=115,y=345)#"删除"按钮

with open("./PatrickStar/version.PatrickStar", "r") as f:  # 打开文件
    awa_1_a = f.read()#获取版本
awa_1 = tk.Label(cnm, text='版本号:{}'.format(awa_1_a), font=('微软雅黑', 5), width=20, height=2)
awa_1.place(x=0,y=3)#打印版本

az_b = tkinter.Listbox(cnm)
az_b.pack(side=tkinter.RIGHT, padx=5, pady=10)

def wc_b_a():
    num_b=0
    with open("./PatrickStar/num.PatrickStar", "r") as f:
        num = f.read()
    num=int(num)
    while num_b==0 :
        num_b=( random.randint(0,num-1))
    b='./PatrickStar/list/{}.PatrickStar'.format(num_b)
    with open(b, "r") as f:
        b_a = f.read()
    az_b.insert(1, "{}".format(b_a))
    tkinter.messagebox.showinfo(title='--Patrick-Star--(直播间抽奖器)', message='中奖者为{}'.format(b_a))

wc_b= tk.Button(cnm, text="抽奖", command=wc_b_a,font=('微软雅黑', 8),bg="#FFFFFF")
wc_b.place(x=350,y=345)

cnm.mainloop() #窗口循环
