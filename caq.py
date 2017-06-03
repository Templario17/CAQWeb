#!/usr/bin/env python 
#-*- coding: utf-8 -*-

#tablas decatipos 

tabla_hombres ={
    1: [None, None, None, 0, 1, 2, 3, (4,5), (6,7), (8,24)],
    2: [None, None, None, 0, None, (1,2), 3, (4,6), (7,9), (10,24)],
    3: [(0,4), 5, (6,7), (8,9), 10, 11, (12,13), (14,15), 16, (17,24)],
    4: [0, 1, 2, (3,4), 5, (6,7), (8,9), (10.11), 12, (13,24)],
    5: [None, 0, 1, (2,3), None, (4,5), (6,7), (8,9), (10,13), (14,24)],
    6: [0, 1, (2,3), (4,6), 7, (8,9), (10,11), (12,13), (14,15), (16,24)],
    7: [None, None, 0, (1,2), None, (3,4), (5,6), 7, (8,10), (11,24)],
    8: [None, 0, 1, (2,3), 4, (5,6), (7,8), (9,10), (11,12), (13,24)],
    9: [(0,7), (8,9), 10, (11,13), 14, (15,16), 17, (18, 19), (18,19), (20,21),(22,24)],
    10:[None, None, 0, (1,2), 3, 4, (5,6), (7,8), (9,11), (12,24)],
    11:[(0,5), 6, (7,8), (9,10), 11, 12, (13,14), 15, (16,17), (18,24)],
    12:[None, 0, 1, (2,3), None, (4,5), (6,7), (8,9), (10,12), (13,24)]
}

tabla_mujeres = {
    1: [None, None, None, 0, 1, 2, (3,4), (5,8), (9,10), (11,24)],
    2: [None, None, None, 0, None, (1,2), (3,4), (5,7), (8,11), (12,24)],
    3: [(0,3), (4,5), (6,7), (8,9), 10, 11, (12,13), (14,15), (16,18), (19,24)],
    4: [0, 1, (2,3), (4,6), 7, (8,9), 10, (11,13), (14,16), (17,24) ],
    5: [None, 0, None, (1,2), 3, (4,6), (7,9), (10,14), (15,17), (18,24)],
    6: [0, (1,2), 3, (4,6), 7, (8,10), (11,12), (13,15), (16,18), (19,24)],
    7: [None, None, 0, (1,2), None, (3,4), 5, (6,7), (8,13), (14,24)],
    8: [None, 0, 1, (2,3), 4, (5,6), (7,8), (9,11), (12,14), (15,24)],
    9: [(0,6), (7,8), 9, (10,12), 13, (14,15), (16,17), (18,19), 20, (20,24)],
    10:[None, None, 0, (1,2), None, (3,4), (5,6), (7,8), (9,12), (13,24)],
    11:[(0,4), (5,6), (7,8), (9,10), 11, 12, (13,14), 15, (16,17), (18,24)],
    # TODO agregar escala 12
}


# TODO terminar diccionario de escalas
dict_escalas = {
        1: 'D1', 2: 'D2', 3: 'D3', 4: 'D4', 5: 'D5', 6: 'D6', 7: 'D7',
        8: 'Pa', 9: 'Pp', 10: 'Sc', 11: 'As', 12: 'Ps'    
}

baremos = {
    'H': tabla_hombres,
    'M': tabla_mujeres
}

escalas = range(1, 13)
sexo = raw_input('Sexo (M/H): ')

resultados = []

# obtener decatipo
for escala in escalas:
    nombre_escala = dict_escalas[escala]
    txt_puntaje = "Puntaje para escala {}: ".format(nombre_escala)
    puntaje = int(raw_input(txt_puntaje))


    fila = baremos[sexo][escala]
    indice = 0

    for e in fila:
        if isinstance(e, int):
            if e == puntaje:
                indice = fila.index(e)
        elif isinstance(e, tuple):
            if puntaje >= e[0] and puntaje <= e[1]:
                indice = fila.index(e)
        
    decatipo = indice + 1
    resultados.append(decatipo)
    
for e in resultados:
    indice_1 = resultados.index(e)
    resul = " {} valor {}".format(e, dict_escalas[indice_1+1])
    print resul    

import matplotlib.pyplot as plt


x = range(1,13)
y = resultados
labels = dict_escalas.values()

plt.plot(x, y, 'ro')
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.1)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()    
    
    
    
