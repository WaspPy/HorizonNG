import serial.tools.list_ports   # pour la communication avec le port série
import struct

lst_keys = ['Time','Phi','Theta','Psi','p','q','r','AccX','AccY','AccZ','Bx','By','Bz','Q0','Q1','Q2','Q3']

# Fonction pour la récupération du port COM utilisé par le capteur

def recup_port_USB() :
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'USB' in p.description :
            mydevice = serial.Serial(p.device,115200, timeout=0.5)

    print(mydevice.is_open) # Affiche et vérifie que le port est ouvert
    print(mydevice.name) # Affiche le nom du port 

    return mydevice


# Fonction pour la récupération des données venant du capteur

def recup_data(mydevice):
    # mydevice.write(b'J')
    # time.sleep(0.035)

    lecture = mydevice.read(mydevice.inWaiting())
    lecture = lecture[2::]

    dico={}
    j = 0
    for i in range(0, len(lecture), 4):  # Découpe de la trame en chaine de 4 octets pour stockage dans dictionnaire
        dico[lst_keys[j]] = struct.unpack('f',lecture[i:i+4])[0]
        j += 1

    return dico

# Fonction limiter la sortie des points cardinaux de l'affichage

def bornesup (val):
    if val<10:
        val=10
    elif val>375:
        val=375
    return val
