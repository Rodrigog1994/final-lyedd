import os

def leer_archivo():
    "crea una lista basada en el archivo csv "
    archivo = open("/home/rodrigo/Escritorio/final/pepe.csv","r")
    lineas = archivo.readlines()

    archivo.close ()
    return lineas



def limpiar_pantalla():
    '''Borra la consola solo para Linux'''
    os.system('clear')


def guardar_datos(lineas):
    """Guarda los datos en distintas listas"""
    Mercado = []
    año = []
    mes = []
    producto = []
    variedad = []
    precio_por_kg = []
    moneda = []
    origen = []

    for linea in lineas[1:]:
        columna = linea.split(",")

        if columna[2] not in Mercado:
            Mercado.append(columna[2])
        if columna[3] not in año:
            año.append(columna[3])
        if columna[4] not in mes:
            mes.append(columna[4])
        if columna[5] not in producto:
            producto.append(columna[5])
        if columna[6] not in variedad:
            variedad.append(columna[6])
        if columna[8] not in precio_por_kg:
            precio_por_kg.append(columna[8])
        if columna[10] not in moneda:
            moneda.append(columna[10].strip())
        if columna[7] not in origen:  
            origen.append(columna[7].strip())

    return Mercado, año, mes, producto, variedad, precio_por_kg, moneda, origen


def mostrar_menu():
    mostrar_encabezado("Bienvenidos al menu interactivo")
    print("\n--- Menú ---")
    print("1. Consultar origen")
    print("2. Consultar precio promedio por producto")
    print("3. Top Ten de productos más caros")
    print("4. Top Ten de productos más baratos")
    print("5. Consultar variedad del producto")
    print("6. Consultar precio por producto" )
    print("7. Mostrar cantidad de registros por producto")
    print("8. Mostrar todas las variedades de producto")
    print("9. Salir")

def consultar_origen():
    lineas = leer_archivo()
    
    nombre_producto = input("Ingrese el nombre del producto para consultar el origen: ")

    for linea in lineas[1:]:
        columna = linea.split(",")

        producto_actual = columna[5].strip().upper()
        origen_actual = columna[7].strip()

        if nombre_producto.upper() == producto_actual:
           renglon = f"El origen del producto '{nombre_producto}' es: {origen_actual}"
           print(f"El origen del producto'{nombre_producto}' es: {origen_actual}")
           return renglon
    
    print(f"No se encontró información sobre el origen para el producto '{nombre_producto}'.")


def consultar_precio_promedio_por_producto(lineas):
    nombre_producto = input("Ingrese el nombre del producto para consultar el precio promedio: ")
    precios = []

    for linea in lineas[1:]:
        columna = linea.split(",")
        producto = columna[5].strip().upper()

        if producto == nombre_producto.strip().upper():
            precio = float(columna[8].strip())
            precios.append(precio)

    if precios:
        precio_promedio = sum(precios) / len(precios)
        
        precio_promedio_formateado = "{:.3f}".format(precio_promedio)
        renglon = f"Precio promedio del producto'{nombre_producto}': {precio_promedio_formateado}"
        print(f"Precio promedio del producto '{nombre_producto}': {precio_promedio_formateado}")
        return renglon
    else:
        print(f"No se encontró información para el producto '{nombre_producto}'.")


def top_diez_productos_mas_caros():
    lineas = leer_archivo()
    renglon =  []
    top_diez = []

    for linea in lineas[1:]:  
        columna = linea.split(",")

        valor = float(columna[8].strip())
            
        if not top_diez or valor > top_diez[-1][1]:
            top_diez.append((columna[5], valor))
            top_diez.sort(key=lambda x: x[1], reverse=True)    
            top_diez = top_diez[:10]

    
    print("Top diez de productos más caros:")
    for i, (producto, precio) in enumerate(top_diez, start=1):
        renglon.append(f"{i}. {producto} - {precio}")
        print(f"{i}. {producto} - {precio}")
    return renglon


def top_diez_productos_mas_baratos():
    lineas = leer_archivo()
    renglon = []
  
    top_diez = []

    for linea in lineas[1:]:  
        columna = linea.split(",")

        
        valor = float(columna[8].strip())
        

        if valor > 0 and (not top_diez or valor < top_diez[-1][1]):
            
            top_diez.append((columna[5], valor))
            top_diez.sort(key=lambda x: x[1])
            top_diez = top_diez[:10]

    
    print("Top diez de productos más baratos:")
    for i, (producto, precio) in enumerate(top_diez, start=1):
        renglon.append(f"{i}. {producto} - {precio}")
        print(f"{i}. {producto} - {precio}")
    return renglon


def consultar_precio():
    
    mes = input("Ingrese el mes en letras: ").lower()
    año = input("Ingrese el año 2017 o 2018: ")
    nombre_producto = input("Ingrese el nombre de la fruta u hortaliza para consultar el precio: ").lower()

    lineas = leer_archivo()

    precio_encontrado = ""

    for linea in lineas[1:]:
        columna = linea.split(",")

        producto = columna[5].strip().lower()
        mes_producto = columna[4].lower()
        año_producto = columna[3]

        if producto == nombre_producto and mes_producto == mes and año_producto == año:
            precio_encontrado = float(columna[8].strip())
            break

    if precio_encontrado:
        renglon = f"Precio del producto '{nombre_producto}' para {mes}/{año}: {precio_encontrado}"
        print(f"Precio del producto '{nombre_producto}' para {mes}/{año}: {precio_encontrado}")
        return renglon
    else:
        print(f"No se encontró precio para el producto '{nombre_producto}' en {mes}/{año}.")

def consultar_variedad():
    
    nombre_producto = input("Ingrese el nombre del producto para consultar la variedad: ")

    lineas = leer_archivo()


    variedad_encontrada = ""

    for linea in lineas[1:]:
        columna = linea.split(",")


        producto = columna[5].strip().upper()
        variedad = columna[6]  

        if producto == nombre_producto.strip().upper():
            variedad_encontrada = variedad
            break  

    if variedad_encontrada:
        renglon = f"Variedad del producto '{nombre_producto}': {variedad_encontrada}"
        print(f"Variedad del producto '{nombre_producto}': {variedad_encontrada}")
        return renglon
    else:
        print(f"No se encontró variedad para el producto '{nombre_producto}'.")


def mostrar_cantidad_registros_por_producto():
    lineas = leer_archivo()
    renglon = []
    
    registros_por_producto = {}

    for linea in lineas[1:]:
        columna = linea.split(",")

        producto = columna[5].strip().upper()

        
        if producto in registros_por_producto:
            registros_por_producto[producto] += 1
        else:
            registros_por_producto[producto] = 1

    if registros_por_producto:
        print("\nCantidad de registros por producto:")
        for producto, cantidad_registros in registros_por_producto.items():
            renglon.append(f"{producto}: {cantidad_registros} registros")
            print(f"{producto}: {cantidad_registros} registros")
    else:
        print("No se encontraron datos en el archivo.")
    return renglon

def mostrar_variedades(lineas):
    variedades = []
    renglon = []
    for linea in lineas[1:]:
        columna = linea.split(",")
        variedad = columna[6].strip()

        if variedad not in variedades:
            variedades.append(variedad)
            renglon.append(variedad)
            print(variedad)
    return renglon

def mostrar_encabezado(texto):
    
    print('┌─' + '─' * len(texto) + '─┐')
    print('│ ' + texto  + ' │')
    print('└─' + '─' * len(texto) + '─┘')
    return

def guardar_busqueda(nombre, renglon):
    nombre_archivo = "consultas.txt"

    with open(nombre_archivo, "a+") as archivo:
        archivo.write(f"{nombre.capitalize()} busco {renglon}. \n")
    print("Los datos se han guardado correctamente en el archivo consultas.txt")

def obtener_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre
nombre_operador = obtener_nombre()


lineas = leer_archivo()
listado_de_variables = guardar_datos (lineas)
    
limpiar_pantalla()


while True:
    limpiar_pantalla()
    
    
    
    mostrar_menu()

    
    opcion = input("Ingrese la opción deseada: ")

    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Error, ingrese un número válido.")
        continue  

    
    if opcion == 1:
        renglon = consultar_origen()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 2:
        renglon = consultar_precio_promedio_por_producto(lineas)
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 3:
        renglon = top_diez_productos_mas_caros()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 4:
        renglon = top_diez_productos_mas_baratos()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 5:
        renglon = consultar_variedad()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 6:
        renglon = consultar_precio()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 7:
        renglon = mostrar_cantidad_registros_por_producto()
        guardar_busqueda(nombre_operador, renglon)
    elif opcion == 8:
        renglon = mostrar_variedades(lineas)
        guardar_busqueda(nombre_operador, renglon)    
    elif opcion == 9:
        print("Hasta luego")
        break  
    else:
        print("Opción inválida. Intente con los números dados.")
    
    input("Presione Enter para continuar...")  








    








    
        





        
