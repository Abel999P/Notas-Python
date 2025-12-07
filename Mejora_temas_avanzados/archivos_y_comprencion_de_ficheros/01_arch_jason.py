
import json

with open('doc.txt') as file:
    data = json.load(file)



try:
    data["clientes1"]
except Exception as e:
    print(f"No se encontro dicho cliente error : {e}")
else:
    print(f"Data encontrada : {data['clientes1']}")

