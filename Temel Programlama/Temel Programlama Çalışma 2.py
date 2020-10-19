from tkinter import*
ekran=Tk()
ekran.title("ADİGEEEEE")
ekran.geometry("500x300")
yazi=Label(text="Sayibir=",fg="Yellow",bg="blue")
yazi1=Label(text="Sayiiki=",fg="Yellow",bg="blue")
yazi3=Label(text="----------------------")
yazi.grid(row=0,column=0)
yazi1.grid(row=1,column=0)
yazi3.grid(row=2,column=1)
girdi1=Entry()
girdi1.grid(row=0,column=1)
girdi2=Entry()
girdi2.grid(row=1,column=1)
sonuc=Label(text="Sonuç=",fg="blue",bg="yellow")
sonuc.grid(row=0,column=2)
sonsonuc=Label(text="Burada görüntülenecek")
sonsonuc.grid(row=1,column=2)
s1=0
s2=0
snc=0
def toplama():
    global s1,s2,snc
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    snc=s1+s2
    sonsonuc["text"]=str(snc)
def cikarma():
    global s1,s2,snc
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    snc=s1-s2
    sonsonuc["text"]=str(snc)
def carpma():
    global s1,s2,snc
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    snc=s1*s2
    sonsonuc["text"]=str(snc)
def bolme():
    global s1,s2,snc
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    snc=s1/s2
    sonsonuc["text"]=str(snc)
top=Button(text="Toplama",command=toplama)
top.grid(row=3,column=0)
cik=Button(text="Çıkarma",command=cikarma)
cik.grid(row=4,column=0)
carp=Button(text="Çapma",command=carpma)
carp.grid(row=3,column=1)
bol=Button(text="Bölme",command=bolme)
bol.grid(row=4,column=1)



