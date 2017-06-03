#!/usr/bin/env python
#-*-coding: utf-8-*-

#resultados decatipos de la prueba guia
resultados = [8, 8, 7, 7, 6, 4, 7, 6, 5, 6, 5, 7]

dict_escalas = {
        1: 'D1', 2: 'D2', 3: 'D3', 4: 'D4', 5: 'D5', 6: 'D6', 7: 'D7',
        8: 'Pa', 9: 'Pp', 10: 'Sc', 11: 'As', 12: 'Ps'
}

#promedio = (4,5,6,7)
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

for n in num:
    if resultados[n] >= 4 and resultados[n]<= 7:
        s = resultados[n]
        print "[*] Decapito {} en promedio normal valor {}".format(dict_escalas[n +1],s)
    elif resultados[n] <= 3:
        s = resultados[n]
        print "[!] Decapito {} BAJO valor = {}".format(dict_escalas[n +1],s)
        print "[*] {}".format(bajos[n + 1])
    else:
        s = resultados[n]
        print "[!] Decapito {} ALTO valor {}".format(dict_escalas[n +1],s)
        print "[*] {}".format(altos[n + 1])



import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
#nombre_file = raw_input('digite nombre del grafico:')
#pp = PdfPages(nombre_file)
#plt.savefig(pp, format='pdf') # dando formato al archivo
#pp.close()
plt.show()

# lo de las axhline lo saque de aqui:
# http://matplotlib.org/examples/pylab_examples/fill_between_demo.html

#TODO hacer iteracion del nombre de las escalas
