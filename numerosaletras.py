def numero_a_letra(numero):
    indicador = [("",""),("MIL","MIL"),("MILLON", "MILLONES"),("MIL MILLONES","MIL MILLLONES"),("BILLON","BILLONES")]
    entero = int(numero)
    contador = 0
    numero_letras = ""  #Declara la variable que nos va a mostrar el texto representando al numero
    while entero > 0: #mientras que entero sea mayor que 0
        a = entero % 1000 #declara variable a que es cuantos modulos de 1000 entran en en entero  
        if contador == 0: # si el contador es igual a cero
            en_letras = a_cifra(a,1).strip() #en letras usa la funcion a_cifras indicando 'a' como el indice de las listas y 1 o 0 para indicar si es por ejemplo cien o ciento
        else:
            en_letras = a_cifra(a,0).strip() #la funcion strip le saca los espacios de los extremos
        if a == 0: #va agregando las palabras para q se forme el numero por bloque ej suma la palabra 'un' con 'millon'
            numero_letras = en_letras+" "+numero_letras 
        elif a ==1:
            if contador in (1,3): 
                numero_letras = indicador[contador][0]+" "+numero_letras
            else:
                numero_letras = en_letras+" "+indicador[contador][0]+" "+numero_letras
        else:
            numero_letras = en_letras+" "+indicador[contador][1]+" "+numero_letras
        numero_letras = numero_letras.strip()
        contador = contador + 1
        entero = int(entero/1000)
    numero_letras = numero_letras

	
    print("numero: ",numero)
    return(numero_letras)
	

def a_cifra(numero,sw):
    lista_centerna = ["",("CIEN","CIENTO"),"DOSCIENTOS", "TRESCIENTOS","CUATROCIENTOS", "QUINIENTOS","SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    lista_decena = ["",("DIEZ","ONCE","DOCE","TRECE","CATORCE","QUINCE","DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE"),("VEINTE","VEINTI"),("TREINTA","TREINTA Y"),("CUARENTA", "CUARENTA Y"),("CINCUENTA","CINCUENTA Y"),("SESENTA", "SESENTA Y"),("SETENTA", "SETENTA Y"),("OCHENTA","OCHENTA Y"),("NOVENTA","NOVENTA Y")]
    lista_unidad = ["",("UN","UNO"),"DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE"]
    centena = int(numero/100)
    decena = int((numero -(centena * 100))/10)
    unidad = int(numero -(centena * 100 + decena * 10))


    texto_centena = ""
    texto_decena = ""
    texto_unidad = ""


    texto_centena = lista_centerna[centena]
    if centena == 1:
        if(decena + unidad)!=0:
            texto_centena=texto_centena[1]
        else:
            texto_centena = texto_centena[0]
    
    texto_decena = lista_decena[decena]
    if decena == 1:
        texto_decena = texto_decena[unidad]
    elif decena > 1:
        if unidad !=0:
            texto_decena = texto_decena[1]
        else:
            texto_decena = texto_decena[0]
    if decena != 1:
        texto_unidad = lista_unidad[unidad]
        if unidad == 1:
            texto_unidad = texto_unidad[sw]
    return "%s %s %s" %(texto_centena,texto_decena,texto_unidad)




