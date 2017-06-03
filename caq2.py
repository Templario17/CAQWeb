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
    12:[None, None, 0, (1,3), None, (4,5), (6,8), (9,10), (11,15), (16,24) ]
}


dict_escalas = {
        1: 'D1', 2: 'D2', 3: 'D3', 4: 'D4', 5: 'D5', 6: 'D6', 7: 'D7',
        8: 'Pa', 9: 'Pp', 10: 'Sc', 11: 'As', 12: 'Ps'
}

dict_nom_escala = { 1:'HIPOCONDRIASIS', 2:'DEPRESION_SUICIDA', 3:'AGITACION',
    4:'DEPRESION_ANSIOSA', 5:'DEPRESION_BAJA_ENERGIA', 6:'CULPABILIDAD-RESENTIMIENTO',
    7:'APATIA', 8:'PARANOIA', 9:'DESVIASION_SICOPATICA', 10:'ESQUISOFRENIA', 
    11:'PSICASTENIA', 12:'DESAJUSTE_PSICOLOGICO' 
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

#imprime en pantalla resultado vs escalas
for e in resultados:
    indice = resultados.index(e)
    resul = "{} valor {}".format(e, dict_escalas[indice+1])
    print resul
# Descripcion de los resultados de la decatipos
altos = {
    1:'Preocupado por su salud, los desarreglos y las funciones corporales',
    2:'Insatisfecho por la vida acoge sentiminetos autodestructivos',
    3:'Incansable busca la exitacion, acepta riesgos, intenta de nuevo',
    4:'Tenso desmañado, manejando algo perturbante, sueños molestos',
    5:'Preocupado, sin energia para actuar, sentiminetos de intraquilidad',
    6:'Autocritico, se acusa de los errores y sentiminetos culpabilidad ',
    7:'Evita contactos interpersonales no se halla confortable con los demas',
    8:'Cree que se le persigue, espia, contrala o maltrate',
    9:'No le ofenden las criticas, acepta lo antisocial en el mismo y en los otros',
    10:'Con impulsos repentinos e incontrolados se aleja de la realidad',
    11:'Le molestan Ideas repotitivas insistentes o habitos compulsivos',
    12:'Timido, pierde su aplomo, con sentimiento de interioridad'
}
bajos = {
    1:'Contento su mente trabaja bien, no tiene temores de salud',
    2:'Satisfecho de la vida y sus aspectos goza de ella',
    3:'Evita situaciones de riesgo, poca necesidad de excitacion ',
    4:'Sosegado, con calma en emergencias, confia en el entorno',
    5:'Energico, muestra entusiamo por el trabajo, sueño profundo',
    6:'No perturbado por culpabilidad o dejar algo importante por hacer',
    7:'Relajado, conciderado y animoso con las personas',
    8:'Confiado, no le afectan los celos o pensamientos de envidia',
    9:'Sensato, evita implicarse en algo ilegal o romper normas',
    10:'Evalua con realidad a las personas, conductas agresivas',
    11:'No le molestan ideas inoportunas o habitos compulsivos',
    12:'Se considera tan apto, confiable y agradable como la mayoria'
}
num = range(0,12)
print "\t\t\t========================"
print "\t\t\t= Descripcion escalas  ="
print "\t\t\t========================"
# salida de la descripcion y lo guarda en archivo de texto 
archivo = "informeCAQ.docx"
for n in num:
    if resultados[n] >= 4 and resultados[n]<= 7:
        s = resultados[n]
        resultado = "[*] {} en promedio normal valor {}\n".format(dict_nom_escala[n +1],s)
        print resultado
        with open (archivo, "a") as f:
            arch = f.write(resultado)          
    elif resultados[n] <= 3:
        s = resultados[n]
        resultado_1 = "[!] {} BAJO valor = {}\n[*] {}\n".format(dict_nom_escala[n +1],s, bajos[n + 1])
        print resultado_1
        with open (archivo, "a") as f:
            arch = f.write(resultado_1)
    else:
        s = resultados[n]
        resultado_2 = "[!] {} ALTO valor {}\n[*] {}\n".format(dict_nom_escala[n +1],s,altos[n + 1])
        print resultado_2
        with open(archivo, "a") as f:
            arch = f.write(resultado_2)


#salida de la grafica con los resultados de las escalas 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from os import system
system("export DISPLAY=:0")

dict_nom_escala = { 1:'HIPOCONDRIASIS', 2:'DEPRESION_SUICIDA', 3:'AGITACION',
    4:'DEPRESION_ANSIOSA', 5:'DEPRESION_BAJA_ENERGIA', 6:'CULPABILIDAD-RESENTIMIENTO',
    7:'APATIA', 8:'PARANOIA', 9:'DESVIASION_SICOPATICA', 10:'ESQUISOFRENIA', 
    11:'PSICASTENIA', 12:'DESAJUSTE_PSICOLOGICO' }

x = range(1, 13)
y = range(1, 11)
labels = dict_escalas.values()
#plt.title('GRAFICA CAQ ')
plt.plot(resultados, x, 'bo', resultados, x)
plt.yticks(x, labels)
plt.xticks(x, y)
plt.grid(True)
plt.axvline(4.5, color='green', lw=2, alpha=0.5)
plt.axvline(6.5, color='green', lw=2, alpha=0.5)
plt.axvline(3.5, color='red', lw=1, alpha=0.7)
plt.axvline(7.5, color='red', lw=1, alpha=0.7)
plt.gca().invert_yaxis()
plt.ylim(13, 0)
plt.xlim(-3, 11)
ax = plt.subplot(111)
ax.xaxis.set_ticks_position('top')
for numero in range(1,13):
    plt.annotate(dict_nom_escala[numero], xy=(-2.8, numero), fontsize=7)
nombre_file = raw_input('Digite nombre del grafico:')
pp = PdfPages(nombre_file) 
plt.savefig(pp, format='pdf') # dando formato al archivo 
pp.close()
plt.show()

# lo de las axhline lo saque de aqui:
# http://matplotlib.org/examples/pylab_examples/fill_between_demo.html
