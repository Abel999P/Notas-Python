
import threading 
import time 


class Hilo(threading.Thread):
    
    def run(self):
        print(f"Inicio : {self.getName()}")
        time.sleep(1)
        print(f"Terminando : {self.getName()}")

if __name__=="__main__":
    
    for i in range(4):
        hilo1 = Hilo(name="Hilo")
        hilo1.start()
        time.sleep(.1)


