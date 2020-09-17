from tkinter import *
from math import sqrt
import math

deg=False
m=0

def log(val,base=None):
    l=(val-1)/(val+1)
    x=l
    y=l
    b=1
    for i in range(1,100):
        x=x*y*y
        l+=x/(2*i+1)
    l*=2
    if base!=None:
        b=log(base)
    return l/b


def sine(val):
    s=val
    x=val
    for i in range(1,100000):
        x=-1*x*val*val/((2*i+1)*2*i)
        s+=x
    return s


def pi():
    return math.pi

def e_val():
    return math.e

def M(val):
    global m
    if val=='+':
        try:
            m+=eval(e.get())
        except:
            s.set('error')
    elif val=='-':
        try:
            m-=eval(e.get())
        except:
            s.set('error')
    elif val=='m':
        s.set(str(m))
    else:
        m=''
        s.set(val)

def press(val):
    if e.get()=='error': s.set('')
    s.set(e.get()+str(val))

def equal(event=None):
    try:
        s.set(eval(e.get()))
    except:
        try:
            s.set(eval(e.get()+')'))
        except:
            s.set('error')

def c():
    s.set('')

def bksp():
    s.set(e.get()[:-1])

def xpown():
    r=e.get()
    st=''
    if len(r)!=0 and r[-1]==')':
        i=len(r)-2
        while(r[i]!='('):
            st=r[i]+st
            i-=1
        r=r[:i]
    else:
        try:
            st=re.search(r'\d+(\.\d+)?$',r).group()
            r=r[:-1*len(st)]
        except:
            s.set('error')
            return
    s.set(r+str('pow('+st+','))

def fact(val):
    if val==1: return 1
    else: return val*fact(val-1)
        
def logpress():
    r=e.get()
    st=''
    if len(r)!=0 and r[-1]==')':
        i=len(r)-2
        while(r[i]!='('):
            st=r[i]+st
            i-=1
        r=r[:i]
    else:
        try:
            st=re.search(r'\d+(\.\d+)?$',r).group()
            r=r[:-1*len(st)]
        except:
            s.set('error')
            return
    s.set(r+str('log('+st+','))

def sin(val):
    if deg==True:
        val=val*pi()/180
    s=sine(val)
    return s

def cos(val):
    if deg==True:
        val=val*pi()/180
    c=(1-sine(val)**2)**0.5
    val=(val%pi())/pi()
    if val>0.5 and val<1.5:
        c*=-1
    return c

def tan(val):
    if deg==True:
        val=val*pi()/180
    s=sine(val)
    c=(1-s**2)**0.5
    val=(val%pi())/pi()
    if val>0.5 and val<1.5:
        c*=-1
    return s/c

def rad():
    global deg
    deg = not deg
    if deg:
        deg_rad.set('deg')
    else:
        deg_rad.set('rad')

r=Tk()
r.title('Calculator')
s=StringVar()
e=Entry(r,textvariable=s)
e.bind('<Return>',equal)
e.grid(columnspan=10,row=0,ipadx=150)
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
Button(r,image=im4,width=60,height=30,command=lambda: press(str(pi()))).grid(row=1,column=7)
Button(r,text='e',width=7,command=lambda: press(str(e_val()))).grid(row=2,column=7)
Button(r,text='|x|',width=7,command=lambda: press('abs(')).grid(row=3,column=7)
Button(r,text='log',width=7,command=lambda: logpress()).grid(row=4,column=7)
Button(r,text='ln',width=7,command=lambda: press('log(')).grid(row=5,column=7)
r.mainloop()


