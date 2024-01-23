#pywhatkit.sendwhatmsg("+543462632986", "hi", 15,10)
import pywhatkit
import pyautogui as pg
import time
def mandar_mensaje(num:str,sms:str):
    """
     envia el mensaje a ese numero lo ingresaado en el 2do parametro
    mediante la aplicacion de whatapp desde la web ,luego se cierra automaticamente.
    """
   
    pywhatkit.sendwhatmsg_instantly(num, sms)
    sleep(3)
    pg.hotkey('ctrl','w')

