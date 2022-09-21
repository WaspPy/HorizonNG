from tkinter import *
from functions import recup_port_USB, recup_data, bornesup
import math as m
import time

# ================================== Début horizon

def horizon():
  global mydevice

  data = recup_data(mydevice)
  mydevice.write(b'J')
  degrees_psi = data['Psi'] * 180 / 3.14159
  degrees_phi = data['Phi'] * 180 / 3.14159
  sinus_theta = m.sin(data['Theta'])

  # Update Label Content
  my_label.config(text=degrees_psi)

  #### Updating Direction Label Positions ####

  # Update Pos North Label
  Nlbl.place(x=bornesup(200 + 190 * m.sin(data['Psi']-data['Phi'])), y=bornesup(200 + sinus_theta * 200 - 190 * m.cos(data['Psi']-data['Phi'])))
  # Update Pos South Label
  Slbl.place(x=bornesup(200 + 190 * (m.sin(data['Psi']-data['Phi']+2*1.5707963267949))), y=bornesup(200 + sinus_theta * 200 - 190 * (m.cos(data['Psi']-data['Phi']+2*1.5707963267949))))
  # Update Pos East Label
  Elbl.place(x=bornesup(200 + 190 * m.sin(data['Psi']-data['Phi']+1.5707963267949)), y=bornesup(200 + sinus_theta * 200 -190 * m.cos(data['Psi']-data['Phi']+1.5707963267949)))
  # Update Pos West Label
  Wlbl.place(x=bornesup(200 + 190 * m.sin(data['Psi']-data['Phi']-1.5707963267949)), y=bornesup(200 + sinus_theta * 200 - 190 * m.cos(data['Psi']-data['Phi']-1.5707963267949)))

  #### Updating Terre Position ####
  # Roulis terre
  can.itemconfig("terre",start = degrees_phi)
  # Tanguage Terre
  can.coords(terre, -1000, -1000+200*sinus_theta, 1400, 1400+200*sinus_theta)

  #### Updating NSEW Position ####

  # Roulis Axe NSaxis
  can.itemconfig("NSaxis", start=-degrees_psi+degrees_phi)
  # Tanguage NSaxis
  can.coords(NSaxis, -1000, -1000 + 200 * sinus_theta, 1400, 1400 + 200 * sinus_theta)

  # Roulis Axe WEaxis
  can.itemconfig("WEaxis", start=(-1)*degrees_psi+degrees_phi+90)   #Modif à tester
  # Tanguage WEaxis
  can.coords(WEaxis, -1000, -1000 + 200 * sinus_theta, 1400, 1400 + 200 * sinus_theta)

  #### Updating ciel Position ####

  # Roulis ciel
  can.itemconfig("ciel", start=degrees_phi+180)
  # Tanguage Terre
  can.coords(ciel, -1000, -1000 + 200 * sinus_theta, 1400, 1400 + 200 * sinus_theta)

  # Bouclage de la MaJ
  myfen.after(40, horizon)

# ========================================== Fin horizon


# ================================= Fonction Align

def align():
  global mydevice
  mydevice.write(b'R')
  time.sleep(0.04)

# ========================================== Fin Align

# ========================================== Main

# ==================== Init device

mydevice = recup_port_USB()

################################### GUI #################################

# ==================== Init Fen

myfen = Tk()
myfen.title("Horizon artificiel - NG")
can = Canvas(myfen, width=400, height=400, bg='light blue')
can.pack()

# ====================== Init Arcs

terre = can.create_arc(-1000, -1000, 1400, 1400, start=180, extent=-180, fill='orange3', tags='terre')

NSaxis = can.create_arc(-1000, -1000, 1400, 1400, start=0, extent=-180, outline='black', tags='NSaxis')
WEaxis = can.create_arc(-1000, -1000, 1400, 1400, start=90, extent=-180, outline='black', tags='WEaxis')

ciel = can.create_arc(-1000, -1000, 1400, 1400, start=0, extent=-180,outline='white',width=3,fill='lightblue', tags='ciel')

# ====================== Init Align Button

bouton_align = Button(can, text='Alignement', command= align)
bouton_align.pack()
can.create_window(50, 350, window=bouton_align)

# ===================== Init Label for Direction

my_label = Label(can, text='Spam',bg='lightblue', fg='green', bd=2)
my_label.pack()
can.create_window(100, 100, window=my_label)

# ===================== Init Label NSEW

# North label
Nlbl= Label(can,text="N")
Nlbl.pack()
can.create_window(200,10, window=Nlbl)

# South label
Slbl= Label(can,text="S")
Slbl.pack()
can.create_window(200,390, window=Slbl)

# East label
Elbl= Label(can,text="E")
Elbl.pack()
can.create_window(10,190, window=Elbl)

# West label
Wlbl= Label(can,text="W")
Wlbl.pack()
can.create_window(390,190, window=Wlbl)

# Init Recuperation donnée

mydevice.write(b'J')
time.sleep(0.04)
horizon() #Lancement fonction MaJ

myfen.mainloop()

################################### End GUI #################################

