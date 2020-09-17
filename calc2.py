from tkinter import *
from math import *
import math,re

#global variables
listprev=[]
deg=False
i=0
m=0
b=0
equ_flag=False
op_flag=False

def prevnext(sym):
    """get the previous entry to the textbox"""
    global listprev,i,equ_flag
    if sym=='->':
        if i < len(listprev)-1:
            i+=1
            s.set(listprev[i])
    else:
        if i > 0:
            i-=1
            s.set(listprev[i])
    equ_flag=True

def pi():
    """ return the pi value"""
    global op_flag,s,equ_flag
    temp = s.get()
    if temp!='' and temp[-1] not in ['*','-','/','+','('] or temp == 'error':
        s.set(math.pi)
    else:
        s.set(temp+str(math.pi))
    op_flag = True

def e_val():
    """return the exponent standard value e"""
    global op_flag,s,equ_flag
    temp = s.get()
    if (temp!='' and temp[-1] not in ['*','-','/','+','(']) or temp=='error':
        s.set(math.e)
    else:
        s.set(temp+str(math.e))
    op_flag = True

def M(val):
    """ to display the content stored in the memory M
        to add or to substract the current value to the memory M"""
    global m
    if val=='+':
        try:
            m+=eval(s.get())
        except:
            s.set('error')
    elif val=='-':
        try:
            m-=eval(s.get())
        except:
            s.set('error')
    elif val=='m':
        s.set(str(m))
    else:
        m=''
        s.set(val)

def press(val):
    """ when any button is clicked corresponding label is added to text box
        based on value passed to this function"""
    global equ_flag,op_flag,e,b
    #print(val)
    if val in ['*','-','/','+']:
        press2(val)
        equ_flag = False
        return
    if equ_flag:
        s.set('')
        op_flag=False
        equ_flag=False
    if val == '(':
        if s.get()!='' and s.get()[-1] in [str(i) for i in range(10)]:
            s.set((val))
        else:
            s.set(s.get()+str(val))
        b+=1;
    elif val in range(10) or val == '.':
        if s.get()!='' and (op_flag or s.get()[-1]==')'):
            s.set('')
            op_flag = False
        s.set(s.get()+str(val))
    else:
        temp = s.get()
        if temp!='' and temp[-1] not in ['*','-','/','+','('] and val !=')':
            s.set(val)
            b=1
        else:
            if val==')':
                if(temp[-1] in ['*','-','+','/']):
                    return
                op_flag=True
                b-=2
            s.set(temp+val)
            b+=1
    #s.icursor("end")

def press2(val):
    """ when any button is clicked corresponding label is added to text box
        based on value passed to this function"""
    global op_flag
    temp = s.get()
    op_flag = False
    if (temp=='' or temp[-1] != '(') and  temp!='error':
        s.set(s.get()+val)
    
def equal(event=None):
    """evaluates every thing on the text box"""
    global listprev,i,equ_flag,b
    calc_val=s.get()
    for i in range(b):
        calc_val+=')'
    try: s.set(eval(calc_val))
    except: s.set('error')
    else: listprev.append(calc_val)
    equ_flag=True
    b=0
    #s.icursor("end")
    

def c():
    """ clear the text box"""
    global b,op_flag
    b=0
    s.set('')
    op_flag=False

def bksp():
    """remove the previous one entry"""
    global b
    if s.get()=='':
        return
    if s.get()[-1] in '()':
        b-=1
    s.set(s.get()[:-1])

def xpown():
    """will get the previous n number x entered before log is pressed
        and then take another number y
        calculates the x power y to the values"""
    global equ_flag,b
    r=s.get()
    st=''
    equ_flag = False
    if len(r)!=0 and r[-1]==')':
        i=len(r)-2
        while(r[i]!='('):
            st=r[i]+st
            i-=1
        r=r[:i]
        if r!='' and r[-1] not in ['*','+','-','/']:
            st='('+st+')'
        while r!='' and r[-1] not in ['*','+','-','/']:
            st=r[i-1]+st
            i-=1
            r=r[:i]
    else:
        try:
            st=re.search(r'-?\d+(\.\d+)?$',r).group()
            r=r[:-1*len(st)]
            if st[0] == '-' and r != '' and r[-1] not in ['*','+','-','/']:
                st = st[1:]
                r+='-'
        except:
            s.set('error')
            equ_flag=True
            return
    s.set(r+str('pow('+st+','))
    b+=1

def fact(val):
    """ calculate the factorial of a number"""
    if val==1: return 1
    else: return val*fact(val-1)
        
def logpress():
    """will get the previous number x entered before log is pressed
        and then take another number y
        will do the log x to the base y"""
    global equ_flag,b
    r=s.get()
    st=''
    equ_flag = False
    if len(r)!=0 and r[-1]==')':
        i=len(r)-2
        while(r[i]!='('):
            st=r[i]+st
            i-=1
        r=r[:i]
        if r!='' and r[-1] not in ['*','+','-','/']:
            st='('+st+')'
        while r!='' and r[-1] not in ['*','+','-','/']:
            st=r[i-1]+st
            i-=1
            r=r[:i]
    else:
        try:
            st=re.search(r'(-)?\d+(\.\d+)?$',r).group()
            r=r[:-1*len(st)]
            if st[0] == '-' and r != '' and r[-1] not in ['*','+','-','/']:
                st = st[1:]
                r+='-'
        except:
            s.set('error')
            equ_flag=True
            return
    s.set(r+str('log('+st+','))
    b+=1

def sin(val):
    """calculate the sine of the angle/value"""
    if deg==True:
        return math.sin(val*math.pi/180)
    else: return math.sin(val)

def cos(val):
    """ calculate the cosecant of the value"""
    if deg==True:
        return math.cos(val*math.pi/180)
    else: return math.cos(val)

def tan(val):
    """ calculate the tangent of the value"""
    if deg==True:
        return math.tan(val*math.pi/180)
    else: return math.tan(val)

def rad():
    """ the change the angular values to deg/rad"""
    global deg
    deg = not deg
    if deg:
        deg_rad.set('deg')
    else:
        deg_rad.set('rad')




#root window to display the window
r=Tk()
r.title('calculator')
#entry for the textbox to be displayed to take values and display them
s=StringVar()
e=Label(r,textvariable=s,background='white',width='45')
#e.bind('<Return>',equal)
e.grid(columnspan=6,row=0,column=1,ipadx=10)
#the code below to add buttons to the window
Button(r,text='<-',width=7,command=lambda: prevnext('<-')).grid(row=0,column=0)
Button(r,text='->',width=7,command=lambda: prevnext('->')).grid(row=0,column=7)
Button(r,text=0,width=15,command=lambda: press(0)).grid(row=5,column=0,columnspan=2)
Button(r,text=1,width=7,command=lambda: press(1)).grid(row=4,column=2)
Button(r,text=2,width=7,command=lambda: press(2)).grid(row=4,column=1)
Button(r,text=3,width=7,command=lambda: press(3)).grid(row=4,column=0)
Button(r,text=4,width=7,command=lambda: press(4)).grid(row=3,column=2)
Button(r,text=5,width=7,command=lambda: press(5)).grid(row=3,column=1)
Button(r,text=6,width=7,command=lambda: press(6)).grid(row=3,column=0)
Button(r,text=7,width=7,command=lambda: press(7)).grid(row=2,column=2)
Button(r,text=8,width=7,command=lambda: press(8)).grid(row=2,column=1)
Button(r,text=9,width=7,command=lambda: press(9)).grid(row=2,column=0)
Button(r,text='.',width=7,command=lambda: press('.')).grid(row=5,column=2)
Button(r,text='+',width=7,command=lambda: press('+')).grid(row=5,column=3)
Button(r,text='-',width=7,command=lambda: press('-')).grid(row=4,column=3)
im5=PhotoImage(file=r'icons/multiply.png')
Button(r,image=im5,width=60,command=lambda: press('*')).grid(row=3,column=3)
im6=PhotoImage(file=r'icons/division.png')
Button(r,image=im6,width=60,command=lambda: press('/')).grid(row=2,column=3)
Button(r,text='=',width=7,command=lambda: equal()).grid(row=5,column=4)
Button(r,text='AC',width=7,height=3,command=lambda: c()).grid(row=2,column=4,rowspan=2)
im1=PhotoImage(file=r'icons/bksp.png')
Button(r,image=im1,width=60,height=30,command=lambda: bksp()).grid(row=4,column=4)
im2=PhotoImage(file=r'icons/sqrt.png')
Button(r,image=im2,width=60,height=30,command=lambda: press('sqrt(')).grid(row=5,column=5)
Button(r,text='(',width=7,command=lambda: press('(')).grid(row=3,column=5)
Button(r,text=')',width=7,command=lambda: press(')')).grid(row=4,column=5)
im3=PhotoImage(file=r'icons/xpown.png')
Button(r,image=im3,width=60,height=30,command=lambda: xpown()).grid(row=2,column=5)
Button(r,text='M',width=7,command=lambda: M('m')).grid(row=2,column=6)
Button(r,text='M+',width=7,command=lambda: M('+')).grid(row=3,column=6)
Button(r,text='M-',width=7,command=lambda: M('-')).grid(row=4,column=6)
Button(r,text='MRC',width=7,command=lambda: M('')).grid(row=5,column=6)
Button(r,text='sin',width=7,command=lambda: press('sin(')).grid(row=1,column=0)
Button(r,text='cos',width=7,command=lambda: press('cos(')).grid(row=1,column=1)
Button(r,text='tan',width=7,command=lambda: press('tan(')).grid(row=1,column=2)
Button(r,text='sinh',width=7,command=lambda: press('sinh(')).grid(row=1,column=3)
Button(r,text='cosh',width=7,command=lambda: press('cosh(')).grid(row=1,column=4)
Button(r,text='tanh',width=7,command=lambda: press('tanh(')).grid(row=1,column=5)
deg_rad=StringVar()
deg_rad.set('rad')
Button(r,textvariable=deg_rad,width=7,command=lambda: rad()).grid(row=1,column=6)
im4=PhotoImage(file=r'icons/pi.png')
Button(r,image=im4,width=60,height=30,command=lambda: pi()).grid(row=1,column=7)
Button(r,text='e',width=7,command=lambda: e_val()).grid(row=2,column=7)
Button(r,text='|x|',width=7,command=lambda: press('abs(')).grid(row=3,column=7)
Button(r,text='log',width=7,command=lambda: logpress()).grid(row=4,column=7)
Button(r,text='ln',width=7,command=lambda: press('log(')).grid(row=5,column=7)

#to configure the window grid to be displayed
r.grid_columnconfigure(12,weight=1)
r.resizable(False, False)
#mainloop to close on click and to do the operations continuously
r.mainloop()

