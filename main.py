
import pandas as pd
from datetime import timedelta
from datetime import datetime
import pywhatkit
import pyautogui as pg
from funciones import mandar_mensaje
import time

try:
    df = pd.read_excel('clientes.xlsx', index_col=False)
except Exception as e:
    print(e)
fecha_actual = datetime.now()

list_vencimiento_prox = []

for index, element in df.iterrows():
    """recorro registro por registro, para crear una lista,donde la columna couta1...couta3 contenga un string='nopago' 
      luego dependiendo que couta sea se calcula la suma correspondiente a fechacompra+ X dias.
    """
    list1 = []
    list1.append(df.iloc[index]["name"])

    if df.iloc[index]['cuota1'] == "nopago":
        list1.append(df.iloc[index]["fechacompra"]+timedelta(days=30))

    if df.iloc[index]['cuota2'] == "nopago":
        list1.append(df.iloc[index]["fechacompra"]+timedelta(days=60))
    if df.iloc[index]['cuota3'] == "nopago":
        list1.append(df.iloc[index]["fechacompra"]+timedelta(days=90))

    list_vencimiento_prox.append(list1)

for index in list_vencimiento_prox:
    for vencimiento in index[1:]:
        # recorro mi lista "list_vencimiento_prox" que esta formado por listas con los datos nescesarios para enviar por whatapp como sms de texto,
        # u crear un df para almacenarlo como otro excel/pdf/csv...
        if (vencimiento-fecha_actual) <= timedelta(days=7):
            sms_text = f"Cliente: {index[0]}fecha de vencimiento: {datetime.strftime(vencimiento,'%d/%m/%y')}"
            pywhatkit.sendwhatmsg_instantly("+543462516761", sms_text)
