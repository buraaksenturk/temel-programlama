from tkinter import*
ekran=Tk()
ekran.title("Sınava Benzer Soru")
ekran.geometry("500x300+300+300")

def cins():
    pass
yazi1=Label(text="Ürünün Alış Fiyatı")
yazi1.grid(row=0,column=0)
yazi2=Entry()
yazi2.grid(row=1,column=0)

def cins1():
    pass
vo=IntVar()
vo1=Radiobutton(ekran,text="%1",variable=vo,value=1,command=cins1)
vo1.grid(row=1,column=1)
vo2=Radiobutton(ekran,text="%8",variable=vo,value=2,command=cins1)
vo2.grid(row=2,column=1)
vo3=Radiobutton(ekran,text="%18",variable=vo,value=3,command=cins1)
vo3.grid(row=3,column=1)
vyazi=Label(text="Vergi Oranı")
vyazi.grid(row=0,column=1)

def cins2():
    pass
    
ko=IntVar()
ko1=Radiobutton(ekran,text="%10",variable=ko,value=4,command=cins2)
ko1.grid(row=1,column=2)
ko2=Radiobutton(ekran,text="%20",variable=ko,value=5,command=cins2)
ko2.grid(row=2,column=2)
ko3=Radiobutton(ekran,text="%30",variable=ko,value=6,command=cins2)
ko3.grid(row=3,column=2)
kyazi=Label(text="Kar Oranı")
kyazi.grid(row=0,column=2)

yazi3=Label(text="Ürünün Son Fiyatı:")
yazi4=Label(text="Ürünün Vergi Oranı:")
yazi5=Label(text="Ürünün Kar Oranı")
yazi3.grid(row=4,column=1)
yazi4.grid(row=5,column=1)
yazi5.grid(row=6,column=1)

karson=0
vergison=0
tson=0
def sonhesap():
    global vergison
    if vo.get()==1:
        vergison=int(yazi2.get())*1/100
        print(vergison)
        yazi4["text"]="Ürünün Vergi Oranı: "+str(vergison)
    if vo.get()==2:
        vergison=int(yazi2.get())*8/100
        print(vergison)
        yazi4["text"]="Ürünün Vergi Oranı: "+str(vergison)
    if vo.get()==3:
        vergison=int(yazi2.get())*18/100
        print(vergison)
        yazi4["text"]="Ürünün Vergi Oranı: "+str(vergison)
    global karson
    if ko.get()==4:
        karson=int(yazi2.get())*10/100
        print(karson)
        yazi5["text"]="Ürünün Kar Oranı: "+str(karson)
    if ko.get()==5:
        karson=int(yazi2.get())*20/100
        print(karson)
        yazi5["text"]="Ürünün Kar Oranı: "+str(karson)
    if ko.get()==6:
        karson=int(yazi2.get())*30/100
        print(karson)
        yazi5["text"]="Ürünün Kar Oranı: "+str(karson)
    tson=int(yazi2.get())+vergison+karson
    yazi3["text"]="Ürünün Son Fiyatı: ",str(tson)
    


yazi6=Button(text="Hesapla",fg="Blue",bg="Yellow",command=sonhesap)
yazi6.grid(row=7,column=1)




