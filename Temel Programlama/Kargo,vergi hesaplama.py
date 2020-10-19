from tkinter import*
ekran=Tk()
ekran.title("Birinci")
ekran.geometry("600x600+300+300")

urunfiyat=Label(text="ÜRÜNÜN FİYATI")
urunfiyat.grid(row=0,column=1)

fgir=Entry()
fgir.grid(row=1,column=1)

koran=Label(text="KAR ORANI(%10)")
koran.grid(row=2,column=1)

kargir=Entry()
kargir.grid(row=3,column=1)

urunadet=Label(text="ÜRÜNÜN ADETİ")
urunadet.grid(row=4,column=0)

urungir=Entry()
urungir.grid(row=4,column=1)

def yap():
    pass

#vergi
vergi=IntVar()
vergi1=Label(text="Vergi oranı")
vergi1.grid(row=0,column=3)

vergi2=Radiobutton(ekran,text="%8",variable=vergi,value=1,command=yap)
vergi2.grid(row=1,column=3)

vergi3=Radiobutton(ekran,text="%18",variable=vergi,value=2,command=yap)
vergi3.grid(row=2,column=3)

#kargo
kargo=IntVar()
kargo1=Label(text="Kargo Durumu")
kargo1.grid(row=3,column=3)

kargo2=Radiobutton(ekran,text="Var",variable=kargo,value=1,command=yap)
kargo2.grid(row=4,column=3)

kargo3=Radiobutton(ekran,text="Yok",variable=kargo,value=2,command=yap)
kargo3.grid(row=5,column=3)

tfiyat=0
tkdv=0
tkar=0
fiyat=0
kdv=0
kar=0
kargof=0
adet=0
def hesapla():
    tfiyat=int(fgir.get())
    if vergi.get()==1:
        tkdv=int(fgir.get())*8/100
        print(tkdv)
    if vergi.get()==2:
        tkdv=int(fgir.get())*18/100
        print(tkdv)
    tkar=int(kargir.get())
    adet=int(urungir.get())
    fiyat=(tfiyat+tkdv+tkar)*int(urungir.get())
    kdv=tkdv*adet
    kar=tkar*adet
    if kargo.get()==1:
        kargof=int(urungir.get())*10
    if kargo.get()==2:
        kargof=0
        
    tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
    tekdv["text"]="Tek ürün için kdv"+str(tkdv)
    tekkar["text"]="Tek Ürün için kar"+str(tkar)
    topfiyat["text"]="Toplam Fiyat"+str(fiyat)
    topkdv["text"]="Toplam kdv"+str(kdv)
    topkar["text"]="Toplam kar"+str(kar)
    topkargo["text"]="Toplam kargo"+str(kargof)




tekfiyat=Label(text="Tek ürün için Fiyat")
tekfiyat.grid(row=0,column=4)

tekdv=Label(text="Tek ürün için kdv")
tekdv.grid(row=1,column=4)

tekkar=Label(text="Tek Ürün için kar")
tekkar.grid(row=2,column=4)

topfiyat=Label(text="Toplam Fiyat")
topfiyat.grid(row=3,column=4)

topkdv=Label(text="Toplam kdv")
topkdv.grid(row=4,column=4)

topkar=Label(text="Toplam kar")
topkar.grid(row=5,column=4)

topkargo=Label(text="Toplam kargo")
topkargo.grid(row=6,column=4)

hesap=Button(text="HESAPLA",command=hesapla)
hesap.grid(row=7,column=4)
