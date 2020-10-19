from tkinter import*
ekran=Tk()
ekran.title("Döviz Hesaplama Formu")
ekran.geometry("500x300")
yazi1=Label(text="TL=",fg="Blue",bg="Yellow",font=("calibri","15","bold"))
yazi2=Label(text="Euro=",fg="Blue",bg="Yellow",font=("calibri","15","bold"))
yazi3=Label(text="Dolar=",fg="Blue",bg="Yellow",font=("calibri","15","bold"))
yazi4=Label(text="Altın=",fg="Blue",bg="Yellow",font=("calibri","15","bold"))
yazi1.grid(row=0,column=0)
yazi2.grid(row=1,column=0)
yazi3.grid(row=2,column=0)
yazi4.grid(row=3,column=0)
girdi1=Entry()
girdi1.grid(row=0,column=1)
girdi2=Entry()
girdi2.grid(row=1,column=1)
girdi3=Entry()
girdi3.grid(row=2,column=1)
girdi4=Entry()
girdi4.grid(row=3,column=1)




yazi5=Label(text="Kaç Euro",fg="Yellow",bg="Blue",font=("Calibri","10","bold"))
yazi6=Label(text="Kaç Dolar",fg="Yellow",bg="Blue",font=("Calibri","10","bold"))
yazi7=Label(text="Kaç Gram Altın",fg="Yellow",bg="Blue",font=("Calibri","10","bold"))
yazi5.grid(row=1,column=2)
yazi6.grid(row=2,column=2)
yazi7.grid(row=3,column=2)

soneuro=Label(text="Elinizdeki Türk lirasıyla alabileceğiniz Euro fiyatı")
sondolar=Label(text="Elinizdeki Türk lirasıyla alabileceğiniz Dolar fiyatı")
sonaltin=Label(text="Elinizdeki Türk lirasıyla alabileceğiniz Altın Gramı fiyatı")
soneuro.grid(row=1,column=3)
sondolar.grid(row=2,column=3)
sonaltin.grid(row=3,column=3)

s1=0
s2=0
s3=0
s4=0
snc1=0
snc2=0
snc3=0
def hesapla():
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    s3=int(girdi3.get())
    s4=int(girdi4.get())
    snc1=s1/s2
    soneuro["text"]=int(snc1)
    snc2=s1/s3
    sondolar["text"]=int(snc2)
    snc3=s1/s4
    sonaltin["text"]=int(snc3)
hesap=Button(text="Hesapla",command=hesapla)
hesap.grid(row=4,column=1)
