from tkinter import*
ekran=Tk()
ekran.title("Radyo Buton Uygulaması")
ekran.geometry("500x300+300+300")

def cins():
    if cinsiyet.get()==1:
        cyazi["text"]="CİNSİYETİNİZ ERKEK"
    if cinsiyet.get()==2:
        cyazi["text"]="CİNSİYETİNİZ KADIN"
        

cinsiyet=IntVar()
erk=Radiobutton(ekran,text="ERKEK",variable=cinsiyet,value=1,command=cins)
erk.grid(row=0,column=0)

kdn=Radiobutton(ekran,text="KADIN",variable=cinsiyet,value=2,command=cins)
kdn.grid(row=1,column=0)

cyazi=Label(text="Cinsiyetiniz")
cyazi.grid(row=2,column=0)

def cins1():
    if yas.get()==3:
        syazi["text"]="Yaşınız 0-18 arası"
    if yas.get()==4:
        syazi["text"]="Yaşınız 18-25 arası"
    if yas.get()==5:
        syazi["text"]="Yaşınız 25-50 arası"
    if yas.get()==6:
        syazi["text"]="Yaşınız 50+ arası"
yas=IntVar()
yas1=Radiobutton(ekran,text="0-18",variable=yas,value=3,command=cins1)
yas1.grid(row=3,column=0)

yas2=Radiobutton(ekran,text="18-25",variable=yas,value=4,command=cins1)
yas2.grid(row=4,column=0)

yas3=Radiobutton(ekran,text="25-50",variable=yas,value=5,command=cins1)
yas3.grid(row=5,column=0)

yas2=Radiobutton(ekran,text="50+",variable=yas,value=6,command=cins1)
yas2.grid(row=6,column=0)

syazi=Label(text="Yaşınız")
syazi.grid(row=7,column=0)
