"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
## Obtenes Datos

def get_columns(filename):
    values_list = []
    with open(filename) as file:
        for row in file:
            values = row.strip().split('\t')
            values_list.append(values)
    columns_list = list(zip(*values_list))
    return columns_list

data=get_columns('data.csv')


columna_1=list(data[0])
columna_2=list(data[1])
columna_3=list(data[2])
columna_4=list(data[3])
columna_5=list(data[4])


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    lista_numeros=[int(num) for num in columna_2]
    
    return sum(lista_numeros)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    letras_unique=list(set(columna_1))

    cuenta=[]
    for letra in letras_unique:
        cuenta.append((letra, columna_1.count(letra)))
      
    return sorted(cuenta)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    letras_unicas=list(set(columna_1)) 
    
    guardar=[]
    for letra in letras_unicas:
        num=[]
        for index in range(len(columna_1)):
            if columna_1[index]==letra:
                num.append(int(columna_2[index]))
        guardar.append((letra,sum(num)))
        
    return sorted(guardar)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    meses=[]
    for date in columna_3:
        anio, mes , dia = date.split('-')
        meses.append(mes)

    cuentas={}
    for mes in meses:
        if mes in cuentas:
            cuentas[mes] += 1
        else:
            cuentas[mes] = 1
    
    return sorted(list(cuentas.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    lista_unica=list(set([letra for letra in columna_1]))
    lista_tupla=[]

    for letra in lista_unica:
        num=[]
        for i in range(len(columna_1)):
            if columna_1[i]==letra:
                num.append(int(columna_2[i]))
        lista_tupla.append((letra,max(num),min(num)))
        
    return sorted(lista_tupla)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lista=list(map(lambda string: string.split(','), columna_5))  
    lista_total=[string for s in lista for string in s] 

    lista_unica=list(set([string[0:3] for string in lista_total])) 

    conteo=[]
    for string_unique in lista_unica: 
        num=[]
        for string in lista_total:
            if string[0:3]==string_unique:
                num.append(int(string.split(':')[-1]))
        conteo.append((string_unique, min(num), max(num)))
    
    return sorted(conteo)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    lista_tupla=[]
    for i in range(0,10):
        letras=[]
        for index in range(len(columna_2)):
            if i==int(columna_2[index]):
                letras.append(columna_1[index])
        lista_tupla.append((i, letras))
    
    return lista_tupla


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    lista_tupla=[]
    for i in range(0,10):
        letras=[]
        for index in range(len(columna_2)):
            if i==int(columna_2[index]):
                letras.append(columna_1[index])
        lista_tupla.append((i, sorted(list(set(letras)))))

    return lista_tupla


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista=list(map(lambda string: string.split(','), columna_5)) 
    lista_total=[string[0:3] for s in lista for string in s] 

    conteo={}
    for string in lista_total:
        if string in conteo:
            conteo[string]+=1
        else:
            conteo[string]=1
    
    return dict(sorted(conteo.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_tupla=[]
    for index in range(len(columna_1)):
        lista_tupla.append((columna_1[index], len(columna_4[index].split(',')), len(columna_5[index].split(','))))
    
    return lista_tupla


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    columna_4_split=[x.split(',') for x in columna_4]
    letras_unique=list(set([string for s in columna_4_split for string in s]))
    
    diccionario={}
    for letra in letras_unique:
        numeros=[]
        for i in range(len(columna_2)):
            for j in range(len(columna_4[i])):
                if columna_4[i][j]==letra:
                    numeros.append(int(columna_2[i]))
        diccionario[letra]=sum(numeros)
    
    
    
    return dict(sorted(diccionario.items()))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    columna_5_split=[x.split(',') for x in columna_5] 
    letras_unica=list(set(columna_1)) 
    
    Diccionario={} 
    for letra in letras_unica: 
        numeros=[]
        for i in range (len(columna_5_split)):
            if columna_1[i]==letra: 
                for j in range (len(columna_5_split[i])):
                    carac, num =columna_5_split[i][j].split(':') 
                    numeros.append(int(num)) 
        Diccionario[letra]=sum(numeros)
    
    return dict(sorted(Diccionario.items()))  
