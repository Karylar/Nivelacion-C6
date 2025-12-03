# 

def validar():
    correcta = "admin123"
    usuario = input("Contraseña: ")
    
    if correcta == usuario:
        print("Correcto")
    else:
        print("Incorrecto")

# Así la usas:
validar()  