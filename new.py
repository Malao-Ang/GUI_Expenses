from tkinter import *
from tkinter import ttk,messagebox
import csv
from datetime import datetime
#ttk is theme of Tk
GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Malao')
GUI.geometry('720x700+500+50')                                           

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20)  #.pack คือ ติดตั้งปุ่ม GUI หลัก

######MANU################################
menubar = Menu(GUI)
GUI.config(menu=menubar)

#file menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')
#help
def About():
    messagebox.showinfo('About','สวัสดีผู้มาเยือน โปรแกรมนี้เป็นดปรแกรมบันทึกข้อมูลสนใจDonateให้เราไหม(Promtpay:0815593836)')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_cascade(label='About',menu=About)
menubar.add_cascade(label='Donate',menu=About)
#Donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
########################################################################



Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

#กำหนดตัวแแปลรูป
icon_t1 = PhotoImage(file='wallet-1-icon.png')
icon_t2 = PhotoImage(file='money-icon (1).png')
icon_s = PhotoImage(file='Save-icon.png')

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='left')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='left')

F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack()

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    n = v_n.get() #จำนวน

    if expense == '':
        print('No data')
        messagebox.showwarning('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return #ถ้าไม่มีไม่ตเองไปต่อ
    elif price == '':
        messagebox.showwarning('Error','กรุณากรอกข้อมูลราคา')
        return #ถ้าไม่มีไม่ตเองไปต่อ
    elif n == '':
        n = 1

    total = float(price) * float(n)

    try:
        total = float(price)*float(n)
        #.get() คือึงมาจาก v_expense = StringVar()
        print('รายการ : {} ราคา:{} ชิ้น {}'.format(expense,price,n))
        print('ทั้งหมด {} บาท'.format(total))
        text = 'รายการ: {} ราคา: {} บาท\n'.format(expense,total)
        text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(n,total)
        v_result.set(text)
        #clearข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_n.set('')
            
        #บันทึกข้อมูลลงในcsvอย่าลืมimport csv
        today = datetime.now().strftime('%a')#day['Mon']=จันทร์
        print(today)
        stamp = datetime.now()
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transactionid = stamp.strftime('%Y%m%d%H%M%f')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            #withคือสั่งเปิดไฟล์แล้วปิดอัตโรมัตอ'savedata.csv'คือตั้งชื่อไฟล์
            #'a'คือการบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            fw = csv.writer(f)#สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [transactionid,dt,expense,price,n,total]
            fw.writerow(data)
        
        #ทำให้เคอเซอร์กลับไปที่ตำแหน่งช่องแรก
        E1.focus()
        update_table()
    except:
        print('Error')
        messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณใส่เลขผิด')#ข้อความหัวข้อของโปรแกรม
        v_expense.set('')
        v_price.set('')
        v_n.set('')
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณใส่เลขผิด')#ข้อความหัวข้อของโปรแกรม
        #messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณใส่เลขผิด')#ข้อความหัวข้อของโปรแกรม

#ทำห้กดenterได้
GUI.bind('<Return>',Save)#ต้องเพิ่มในdef Save (even=None)ด้วย

font1 = (None,20)#None เปลี่ยนเป็น angsana new

#---------image--------------

main_icon = PhotoImage(file='analytics-icon.png')

Mainicon = Label(F1,image=main_icon)
Mainicon.pack()

#---------text1--------------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=font1).pack()
#สร้างตัวแปลไว้เก็บproduct
v_expense = StringVar()
#StringVar คือตัวแปลพิเศษไว้เก็บข้อมูล GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=font1)
E1.pack()
#-----------endtext1---------

#---------text2--------------
L = ttk.Label(F1,text='ราคา(บาท)',font=font1).pack()
#สร้างตัวแปลไว้เก็บproduct
v_price = StringVar()
#StringVar คือตัวแปลพิเศษไว้เก็บข้อมูล GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=font1)
E2.pack()
#-----------endtext2---------

#---------text3--------------
L = ttk.Label(F1,text='จำนวน(ชิ้น)',font=font1).pack()
#สร้างตัวแปลไว้เก็บproduct
v_n = StringVar()
#StringVar คือตัวแปลพิเศษไว้เก็บข้อมูล GUI
E3 = ttk.Entry(F1,textvariable= v_n,font=font1)
E3.pack()
#-----------endtext3---------

B2 = ttk.Button(F1,text = f'{"Save": >{10}}',image=icon_s,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)
#สร้างfunction เวลาคลิ้กจะได้มีอะไรขึ้นมา คือ def'''

v_result = StringVar()#ข้อความที่สรามาถทำให้เป็น.get .set
v_result.set('---------result--------')
result = ttk.Label(F1,textvariable= v_result,font=font1,foreground='green')

result.pack(pady = 20)
################ tap 2#################


def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data

def update_record():
    getdata = read_csv()

#table
header = ['รหัสรายการ','วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack() 

#for i in range(len(header)): #ใช้รันfor loop เพื่อเขียนหัวข้อก็ได้
    #resulttable.heading('วัน-เวลา',text='date(วันเวลา)') การใส่หัวข้อแบบนี้มันแก้หลายรอบ
    #resulttable.heading(header[i],text=header[i])#ให้อ้างอิงโค้ดมาเลย

for h in header:
    resulttable.heading(h,text=h)

headerwidth = [120,150,170,80,80,80] #ความกว้างคอลั้ม
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)
#resulttable.column('วัน-เวลา',width=10)

#resulttable.insert('',0,value=['จันทร์','น้ำดื่ม',30,35,100])
#resulttable.insert('','end',value=['อังคาร','น้ำดื่ม',30,35,100])

alltransaction = {}

def UpdateCSV():
    with open('savedata.csv','w',newline='',encoding='utf-8') as f:
        fw = csv.writer(f)
        #เตรียมข้อมูลให้กลายเป็นlist
        data = list(alltransaction.values())
        fw.writerows(data) #mutiple line from list[[],[],[]]
        print('Table was update')

def DeleteRecord():
    check = messagebox.askyesno('Confirm','คุณต้องการลบข้อมูลใช่ไหม')
    print('Yes/No',check)
    if check == True:
        print('delete')
        select = resulttable.selection()
        print(select)
        data = resulttable.item(select)
        data = data['values']
        transactionid = data[0]
        print(type(transactionid))
        del alltransaction[str(transactionid)]
        print(transactionid)
        UpdateCSV()
        update_table()
    else:
        print('cancel')


BDelete = ttk.Button(T2,text='delete',command=DeleteRecord)
BDelete.place(x=50,y=550)

resulttable.bind('<Delete>',DeleteRecord)

def update_table():
    resulttable.delete(*resulttable.get_children()) #รหัสพิเศษเป็นการสีั่งลบอัตโนมัติ ลบรัวๆ
    #for c in resulttable.get_children():
     #   resulttable.delete(c)
    try:  
        data = read_csv()
        for d in data:
            #สร้างtransaction data
            alltransaction[d[0]] = d
            resulttable.insert('',0,value=d)
        print(alltransaction)

    except:
        print('No File')
    
update_table()
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()