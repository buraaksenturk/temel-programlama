from tkinter import*
ekran=Tk()
ekran.title("Birinci")
ekran.geometry("600x600+300+300")

urunfiyat=Label(text="ÜRÜNÜN FİYATI")
urunfiyat.grid(row=0,column=0)

fgir=Entry()
fgir.grid(row=1,column=0)

urunadet=Label(text="ÜRÜNÜN ADETİ")
urunadet.grid(row=0,column=1)

urungir=Entry()
urungir.grid(row=1,column=1)

koran=Label(text="KAR ORANI")
koran.grid(row=0,column=2)

kargir=Entry()
kargir.grid(row=1,column=2)

def yap():
    pass

#vergi
vergi=IntVar()
vergi1=Label(text="Vergi oranı")
vergi1.grid(row=0,column=3)

vergi2=Radiobutton(ekran,text="%8",variable=vergi,value=1,command=yap())
vergi2.grid(row=1,column=3)

vergi3=Radiobutton(ekran,text="%18",variable=vergi,value=2,command=yap())
vergi3.grid(row=2,column=3)

#kargo
kargo=IntVar()
kargo1=Label(text="Kargo Durumu")
kargo1.grid(row=0,column=4)

kargo2=Radiobutton(ekran,text="Var",variable=kargo,value=1,command=yap())
kargo2.grid(row=1,column=4)

kargo3=Radiobutton(ekran,text="Yok",variable=kargo,value=2,command=yap())
kargo3.grid(row=2,column=4)

tfiyat=0
tkdv=0
tkar=0
fiyat=0
kdv=0
kar=0
kargof=0
def hesapla():

    if vergi.get()==1 and kargo.get()==1:
        tfiyat=int(fgir.get())+(int(fgir.get())*int(kargir.get())/100)+(int(fgir.get())*8/100)
        tkdv=int(fgir.get())*8/100
        tkar=int(fgir.get())*int(kargir.get())/100
        fiyat=int(urungir.get())*tfiyat
        kdv=int(urungir.get())*tkdv
        kar=int(urungir.get())*tkar

        if tfiyat<1000 and fiyat<1000:
            tfiyat=tfiyat+10
            fiyat=fiyat+(int(urungir.get())*10)
            kargof=(int(urungir.get())*10)
            print(fiyat)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam Fiyat"+str(fiyat)
            topkdv["text"]="Toplam kdv"+str(kdv)
            topkar["text"]="Toplam kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)
            

        if tfiyat<1000 and fiyat>=1000:
            tfiyat=tfiyat+10
            fiyat=fiyat
            kargof=10
            print(fiyat)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam Fiyat"+str(fiyat)
            topkdv["text"]="Toplam  kdv"+str(kdv)
            topkar["text"]="Toplam  kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)

        if tfiyat>=1000 and fiyat>=1000:
            tfiyat=tfiyat
            fiyat=fiyat
            kargof=0
            print(fiyat)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam  Fiyat"+str(fiyat)
            topkdv["text"]="Toplam  kdv"+str(kdv)
            topkar["text"]="Toplam kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)

    if vergi.get()==1 and kargo.get()==2:
        tfiyat=int(fgir.get())+(int(fgir.get())*int(kargir.get())/100)+(int(fgir.get())*8/100)
        tkdv=int(fgir.get())*8/100
        tkar=int(fgir.get())*int(kargir.get())/100
        fiyat=int(urungir.get())*tfiyat
        kdv=int(urungir.get())*tkdv
        kar=int(urungir.get())*tkar
        kargof=0
        
        print(fiyat)
        tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
        tekdv["text"]="Tek ürün için kdv"+str(tkdv)
        tekkar["text"]="Tek Ürün için kar"+str(tkar)
        topfiyat["text"]="Toplam  Fiyat"+str(fiyat)
        topkdv["text"]="Toplam kdv"+str(kdv)
        topkar["text"]="Toplam kar"+str(kar)
        topkargo["text"]="Toplam kargo"+str(kargof)
            

    if vergi.get()==2 and kargo.get()==1:
        tfiyat=int(fgir.get())+(int(fgir.get())*int(kargir.get())/100)+(int(fgir.get())*18/100)
        tkdv=int(fgir.get())*18/100
        tkar=int(fgir.get())*int(kargir.get())/100
        fiyat=int(urungir.get())*tfiyat
        kdv=int(urungir.get())*tkdv
        kar=int(urungir.get())*tkar

        if tfiyat<1000 and fiyat<1000:
            tfiyat=tfiyat+10
            fiyat=fiyat+(int(urungir.get())*10)
            print(fiyat)
            kargof=(int(urungir.get())*10)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam Fiyat"+str(fiyat)
            topkdv["text"]="Toplam kdv"+str(kdv)
            topkar["text"]="Toplam kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)
            

        if tfiyat<1000 and fiyat>=1000:
            tfiyat=tfiyat+10
            fiyat=fiyat
            kargof=10
            print(fiyat)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam  Fiyat"+str(fiyat)
            topkdv["text"]="Toplam  kdv"+str(kdv)
            topkar["text"]="Toplam kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)

        if tfiyat>=1000 and fiyat>=1000:
            tfiyat=tfiyat
            fiyat=fiyat
            kargof=0
            print(fiyat)
            tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
            tekdv["text"]="Tek ürün için kdv"+str(tkdv)
            tekkar["text"]="Tek Ürün için kar"+str(tkar)
            topfiyat["text"]="Toplam Fiyat"+str(fiyat)
            topkdv["text"]="Toplam kdv"+str(kdv)
            topkar["text"]="Toplam kar"+str(kar)
            topkargo["text"]="Toplam kargo"+str(kargof)

    if vergi.get()==2 and kargo.get()==2:
        tfiyat=int(fgir.get())+(int(fgir.get())*int(kargir.get())/100)+(int(fgir.get())*18/100)
        tkdv=int(fgir.get())*18/100
        tkar=int(fgir.get())*int(kargir.get())/100
        fiyat=int(urungir.get())*tfiyat
        kdv=int(urungir.get())*tkdv
        kar=int(urungir.get())*tkar
        kargof=0
        
        print(fiyat)
        tekfiyat["text"]="Tek ürün için Fiyat"+str(tfiyat)
        tekdv["text"]="Tek ürün için kdv"+str(tkdv)
        tekkar["text"]="Tek Ürün için kar"+str(tkar)
        topfiyat["text"]="Toplam Fiyat"+str(fiyat)
        topkdv["text"]="Toplam  kdv"+str(kdv)
        topkar["text"]="Toplam  kar"+str(kar)
        topkargo["text"]="Toplam kargo"+str(kargof)


tekfiyat=Label(text="Tek ürün için Fiyat")
tekfiyat.grid(row=4,column=1)

tekdv=Label(text="Tek ürün için kdv")
tekdv.grid(row=5,column=1)

tekkar=Label(text="Tek Ürün için kar")
tekkar.grid(row=6,column=1)

topfiyat=Label(text="Toplam Fiyat")
topfiyat.grid(row=7,column=1)

topkdv=Label(text="Toplam kdv")
topkdv.grid(row=8,column=1)

topkar=Label(text="Toplam kar")
topkar.grid(row=9,column=1)

topkargo=Label(text="Toplam kargo")
topkargo.grid(row=10,column=1)

hesap=Button(text="HESAPLA",command=hesapla)
hesap.grid(row=11,column=1)
