contador_legendario = 0
contador_entrenamiento = 0

while True:
    try:
        cantidad_aspirantes = int(input("cuantos aspirantes a Superheroes se registran...."))

        if cantidad_aspirantes>0:
            print("Registrar un superheroe....")
            
            for i in range(cantidad_aspirantes):
                while True:
                    nombre = input("ingrese un alias:")
                    if  len(nombre) < 7 or " " in nombre:
                         print("Alias invalido. Intente nuevamente.")
                    else:
                        break
            
                while true:
                    poder = int(input("ingrese el poder:"))
                    if poder <= 0:
                        print("Nivel invalido. Debe ingressr un entero positivo.")
                    else:
                        break
            
                if poder >= 90:
                    contador_legendario += 1
                else:
                    contador_entrenamiento += 1
            
            print(f"Se registraron {contador_legendario} Heroe(s) Legendarios y {contador_entrenamiento} Heroe(s) en Entrenamiento.")
          #comntario  
            break
        else:
            print("Cantidad invalida. Debe ingresar un entero positivo.")
    except:
        print("Es invalido lo que ingresaste...")
        
