"""T

inker. pysimple
augstaka limen joslais ir konkretas lietas kas jadara pa soliem


! importejiet tkinter moduli
2 izveidojiet galveno lietotaj programmas logu
3 pievienojie logam logrikus,piemeram etiketes, pogas, ramjus utt.
4 izsauciet galveno notikumu ciļnu lai darbibas varetu veikt lietotaja

logrīki jeb widgets

"""
from tkinter import*
 #vai
#import tkinter as Sanija !!!
#logs=Sanija.Tk() !!!!!!!!!!!


#izveidojam galveno logriku
# PACK METODE

"""logs=Tk()
logs.iconbitmap("ok.ico")

sarkana_poga=Button(logs, text="Sarkana", fg="red")
sarkana_poga.pack(side=LEFT)


Zila_poga=Button(logs, text="Zila", fg="blue")
Zila_poga.pack(side=RIGHT)


Zaļa_poga=Button(logs, text="Zaļa", fg="green")
Zaļa_poga.pack(side=RIGHT)


dzeltena_poga=Button(logs, text="Dzeltena", fg="yellow")
dzeltena_poga.pack(side=LEFT)
#uzmet mazu lodžiņu
logs.mainloop()"""

# GRID METODE
#-jāzin kollona un rinda- apzime ar nulli

logs=Tk()
logs.iconbitmap("ok.ico")

sarkana_poga=Button(logs, text="❤", fg="red")
sarkana_poga.grid(row=0, column=0)


Zila_poga=Button(logs, text="❤", fg="blue")
Zila_poga.grid(row=0, column=10)


Zaļa_poga=Button(logs, text="❤", fg="green")
Zaļa_poga.grid(row=10, column=0)


dzeltena_poga=Button(logs, text="❤", fg="yellow")
dzeltena_poga.grid(row=10, column=10)
#uzmet mazu lodžiņu


# pielikt label logam
nosaukums1=Label(logs,text="Vārds").grid(row=5, column=5)
ievads1=Entry(logs).grid(row=5, column=6)



# PLACE METODE

"""logs=Tk()
logs.iconbitmap("ok.ico")

sarkana_poga=Button(logs, text="❤", fg="red")
sarkana_poga.place(x=100, y=200)


Zila_poga=Button(logs, text="❤", fg="blue")
Zila_poga.place(x=300, y=50)


Zaļa_poga=Button(logs, text="❤", fg="green")
Zaļa_poga.place(x=100, y=400)


dzeltena_poga=Button(logs, text="❤", fg="yellow")
dzeltena_poga.place(x=100, y=59)

# pielikt label logam
nosaukums1=Label(logs,text="Vārds").place(x=50, y=100)
ievads1=Entry(logs).grid(row=1, column=2)"""

# change background color
logs.configure(bg="#B67070") 
logs.mainloop()
"""logs.iconbitmap("Ōk.ico")#pieskir ikonu ig
#logs.geometry("400x300+100+50")# cik liels tab
logs.title("Šis ir loga nosaukums")
"""

#ka nomainit ikonnu?
#tris geometrijas metodes:
"""

pakošanas metode-   
1. defineju podu

"""

