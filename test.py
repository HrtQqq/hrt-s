from tkinter import *

def callback():
    var.set('是真的')

root = Tk()
root.title('猪猪检测')

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('MKK是小猪')

# 将图片实例化
photo = PhotoImage(file="1.png")    

#justify是设置对齐  ，compound是设置字体浮于文字上方
theLable = Label(frame1,textvariable = var,justify=LEFT,image = photo,compound=CENTER,font=('微软黑体',20),fg='black')
theLable.pack(side = LEFT)

thebutton = Button(frame2,text='是真的吗？',COMMAND = callback())
thebutton.pack()

frame1.pack()
frame2.pack()
mainloop()
