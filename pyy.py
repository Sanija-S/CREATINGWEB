import tkinter as tk
from tkinter import messagebox
"""def parādi_sveicienu():  # 1.janolasa no ta teksta laucina kas to ieraksta, ig submitojot paradas jauns logs
    vards=ievades_lauks.get()# no teksta lauka getto vertibu
    messagebox.showinfo("Sveiciens! " f"Labdien, {vards}!")  # svarigi message boksu importet # 1. iekavās- jabut loga nosaukumam, 2. pievienoju tekstu ko pateiks, "{}" pievienojot usera ievadīto lauku

logs=tk.Tk()
logs.title("Message responder tab")
# ievades lauku vards ievadisanai
ievade=tk.Label=("Ievadi")
ievade=tk.Entry(logs, width= 30)
ievade.pack(pady=10)# parametrs kas nosaka vertikalu atstarpi starp loga elementiem

# poga, lai izsauktu sveiciena logu
sveiciens_poga=tk.Button(logs, text="Sveiciens", command=parādi_sveicienu)# is jaaktivize poga ar komandu: "command=parādi_sveicienu"
sveiciens_poga.pack(pady=10)

logs.configure(bg="#ADD8E6") 
logs.mainloop()"""


def milaka_krasa():  # 1.janolasa no ta teksta laucina kas to ieraksta, ig submitojot paradas jauns logs
    krasa=ievades_lauks.get()# no teksta lauka getto vertibu
    messagebox.showinfo("Es zinu tavu mīļāko krāsu! " f"Vai tā ir {krasa}?")

    
logs=tk.Tk()
logs.title("Message responder tab")
# ievades lauku vards ievadisanai
ievades_lauks=tk.Entry(logs, width= 30)
ievades_lauks.pack(pady=10)# parametrs kas nosaka vertikalu atstarpi starp loga elementiem

# poga, lai izsauktu sveiciena logu
sveiciens_poda=tk.Button(logs, text="Sveiciens", command=milaka_krasa)# is jaaktivize poga ar komandu: "command=parādi_sveicienu"
sveiciens_poda.pack(pady=10)

logs.configure(bg="#FFB6C1") 

logs.mainloop()