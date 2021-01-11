from colas import BoundedPriorityQueue

print("Pruebas de colas con prioridad acotada")
maestres = {"prioridad": 4, "descripcion":"Maestre", "personas":["Aemon", "Luwin"]}
niños = {"prioridad": 2, "descripcion":"Niños", "personas":["Santi", "Angel"]}
mecanicos = {"prioridad": 4, "descripcion":"Mecanicos", "personas":["Diana", "Maria"]}
mujeres = {"prioridad": 3, "descripcion": "Mujeres", "personas":["Mariana", "Sofia"]}
tercera = {"prioridad": 2, "descripcion": "Tercera edad", "personas":["Victor"]}
ninas = {"prioridad": 1, "descripcion": "Niñas", "personas":["Alejandra", "Monse", "Tania"]}
hombres = {"prioridad": 3, "descripcion": "Hombres", "personas":["Luis", "Javier"]}
vigia = {"prioridad": 4, "descripcion": "Vigia", "personas":["Jon", "Sam"]}
capitan = {"prioridad": 5, "descripcion": "Capitan", "personas":["Rafa"]}
timonel = {"prioridad": 4, "descripcion": "Timonel", "personas":["Raul"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(tercera['prioridad'], tercera)
cpa.enqueue(ninas['prioridad'], ninas)
cpa.enqueue(hombres['prioridad'], hombres)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)
cpa.to_string()

print("")
print("Las niñas han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los niños han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los adultos de la 3° edad han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Las mujeres han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los hombres han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los maestres han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los mecanicos han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("Los vigias han dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("El timonel ha dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("El capitan ha dejado el barco")
cpa.dequeue()
cpa.to_string()
print("")
print("El barco fue evacuado por completo")
print("")
cpa.dequeue()
cpa.dequeue()
