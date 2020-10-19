from tkinter import*
ekran=Tk()
ekran.title("ybs")
ekran.geometry("600x600+200+200")

hamm=Label(text="Ham Maaş")
hamm.grid(row=1,column=1)

maas=Entry()
maas.grid(row=1,column=2)

mesais=Label(text="Mesai Saati")
mesais.grid(row=2,column=1)

mesai=Entry()
mesai.grid(row=2,column=2)

aile=IntVar()
vergi=IntVar()

def yap():
    pass

av=Radiobutton(ekran,text="Aile Yardımı Var",variable=aile,value=1,command=yap)
av.grid(row=3,column=1)
ay=Radiobutton(ekran,text="Aile Yardımı Yok",variable=aile,value=2,command=yap)
ay.grid(row=4,column=1)
v10=Radiobutton(ekran,text="%10",variable=vergi,value=1,command=yap)
v10.grid(row=1,column=3)
v15=Radiobutton(ekran,text="%15",variable=vergi,value=2,command=yap)
v15.grid(row=2,column=3)


pkm=Label(text="Personelin Kesintisiz Maaşı")
pkm.grid(row=3,column=3)
vk=Label(text="Vergi Kesintisi")
vk.grid(row=4,column=3)
pksm=Label(text="Pesonelin Kesintili Son Maaşı")
pksm.grid(row=5,column=3)

mesai1=0
prim=0
ailey=0
sonmaas=0
toplam1=0
toplam2=0
toplam3=0
def hesapla():
    mesai1=int(maas.get())+(int(mesai.get())*25)
    if vergi.get()==1:
        prim=int(mesai1)+(int(maas.get())*10/100)
    if vergi.get()==2:
        prim=int(mesai1)+(int(maas.get())*15/100)
    if aile.get()==1:
        sonmaas=int(prim)+250
    if aile.get()==2:
        sonmaas=int(prim)+0
    toplam1=int(sonmaas)
    if toplam1<5000:
        toplam2=int(toplam1)*15/100
    if toplam1>=5000 and toplam1<=8000:
        toplam2=int(toplam1)*20/100
    if toplam1>8000:
        toplam2=int(toplam1)*30/100
    toplam3=int(toplam1)-int(toplam2)
    pkm["text"]="Personelin Kesintisiz Maaşı"+str(toplam1)
    vk["text"]="Vergi Kesintisi"+str(toplam2)
    pksm["text"]="Pesonelin Kesintili Son Maaşı"+str(toplam3)

hesap=Button(text="HESAPLA",command=hesapla)
hesap.grid(row=6,column=3)


