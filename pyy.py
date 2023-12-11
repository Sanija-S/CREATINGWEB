import tkinter as tk
logs=tk.Tk()
logs.title("Sveiciens visiem")
# ievades lauku vards ievadisanai
ievades_lauks=tk.Entry(logs, width= 30)
ievades_lauks.pack(pady=10)# parametrs kas nosaka vertikalu atstarpi starp loga elementiem

logs.mainloop()



# poga, lai izsauktu sveiciena logu
sveociens_poda=tk.Button(logs, text="Sveiciens")
sveociens_poda.pack(pady=10)
