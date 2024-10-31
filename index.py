productos = []


while True:
    print("bienvenido, ¿que desea hacer? ")
    print ("1. Agregar un producto nuevo")
    print ("2. Mostrar los rpoductos registrados")
    print ("3. Salir")


    opcion = input ("Elige una opcion ") 

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")

        cantidad = int(input ("Ingrese la cantidad: "))

        
      
        producto = [ producto, cantidad]

        productos.append(producto)
    
    
        print(f"Producto: {producto},  agregado exitosamente.")
      

    elif opcion == "2":
        indice = 0 
        while indice < len(productos):
            print(f"producto:  {productos[indice][0]}, Cantidad: {productos[indice][1]}")

            indice += 1

    elif opcion == "3":
        print("Saliendo del programa. Gracias!")
        break
    
    else:
        print("Opcion no valida, por favor elige 1, 2, ó 3")


