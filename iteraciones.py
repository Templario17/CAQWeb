#-*-coding: utf-8-*-
# def funcion(cadena, numero, cadena2):
#     print cadena, numero, cadena2
#
# dict_nom_escala = { 1:'HIPOCONDRIASIS', 2:'DEPRESION_SUICIDA', 3:'AGITACION',
#     4:'DEPRESION_ANSIOSA', 5:'DEPRESION_BAJA_ENERGIA', 6:'CULPABILIDAD-RESENTIMIENTO',
#     7:'APATIA', 8:'PARANOIA', 9:'DESVIASION_SICOPATICA', 10:'ESQUISOFRENIA',
#     11:'PSICASTENIA', 12:'DESAJUSTE_PSICOLOGICO' }
#
# variable = 'FRONSIZE'
# # multiplo: multiplos de 5, en sucesión progresiva comenzando en 5
# for multiplo in range(1,13):
#     funcion(dict_nom_escala[multiplo], multiplo, variable)
resultados = [8, 3, 9, 7, 5, 4, 7, 2, 5, 8, 5, 1]

dict_nom_escala = { 1:'HIPOCONDRIASIS', 2:'DEPRESION_SUICIDA', 3:'AGITACION',
    4:'DEPRESION_ANSIOSA', 5:'DEPRESION_BAJA_ENERGIA', 6:'CULPABILIDAD-RESENTIMIENTO',
    7:'APATIA', 8:'PARANOIA', 9:'DESVIASION_SICOPATICA', 10:'ESQUISOFRENIA',
    11:'PSICASTENIA', 12:'DESAJUSTE_PSICOLOGICO' }

dict_escalas = {
        1: 'D1', 2: 'D2', 3: 'D3', 4: 'D4', 5: 'D5', 6: 'D6', 7: 'D7',
        8: 'Pa', 9: 'Pp', 10: 'Sc', 11: 'As', 12: 'Ps'
}
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
            
#guardar en archivo de texto
 
    
 
 
        
