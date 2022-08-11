from tkinter import *

def buttonPlus():
    Zahl1=float(entryZahl1.get())
    Zahl2=float(entryZahl2.get())
    Ergebnis=Zahl1+Zahl2
    labelOutput.config(text=Ergebnis)

Fenster=Tk()
Fenster.title("Plus rechnen")
Fenster.geometry("400x300")

labelZahl1=Label(master=Fenster, bg="#3FC031", text="Erste Zahl")
labelZahl1.place(x=60, y=30, width=100, height=30)

entryZahl1=Entry(master=Fenster, bg="white")
entryZahl1.place(x=200, y=30, width=100, height=30)

labelZahl2=Label(master=Fenster, bg="#3FC031", text="Erste Zahl")
labelZahl2.place(x=60, y=70, width=100, height=30)

entryZahl2=Entry(master=Fenster, bg="white")
entryZahl2.place(x=200, y=70, width=100, height=30)

buttonBerechnen=Button(master=Fenster, bg="#3FC031", text="Addieren", command=buttonPlus())
buttonBerechnen.place(x=60, y=110, width=100, height=30)

labelErgebnis=Label(master=Fenster, bg="#3FC031", text="Ergebnis")
labelErgebnis.place(x=60, y=140, width=100, height=30)

labelOutput=Label(master=Fenster, bg="white", text="")
labelOutput.place(x=200, y=140, width=100, height=30)

Fenster.mainloop()