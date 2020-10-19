from tkinter import*
ekran=Tk()
ekran.title("ADİGEEEEE")
ekran.geometry("500x300")
yazi=Label(text="Ürünün Fiyatı=",fg="Yellow",bg="blue")
yazi1=Label(text="Kar Oranı(%)=",fg="Yellow",bg="blue")
yazi2=Label(text="KDV Oranı(%)",fg="Yellow",bg="blue")
cizgi1=Label(text="----------------------")
cizgi2=Label(text="----------------------")
cizgi3=Label(text="----------------------")
yazi.grid(row=0,column=0)
yazi1.grid(row=1,column=0)
yazi2.grid(row=2,column=0)
cizgi1.grid(row=3,column=1)
cizgi2.grid(row=3,column=0)
girdi1=Entry()
girdi1.grid(row=0,column=1)
girdi2=Entry()
girdi2.grid(row=1,column=1)
girdi3=Entry()
girdi3.grid(row=2,column=1)
sonuc=Label(text="Sonuç=",fg="blue",bg="yellow")
sonuc.grid(row=4,column=1)
sonsonuc=Label(text="Burada görüntülenecek")
sonsonuc.grid(row=5,column=1)
s1=0
s2=0
s3=0
snc=0
def hesapla():
    s1=int(girdi1.get())
    s2=int(girdi2.get())
    s3=int(girdi3.get())
    snc=s1+(s2/100)+(s3/100)
    sonsonuc["text"]=str(snc)

hesap=Button(text="Hesapla",command=hesapla)
hesap.grid(row=4,column=0)



