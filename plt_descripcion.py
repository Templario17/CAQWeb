#/usr/bin/env python 
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
t = "texto prueba para la descripcion del caq"
plt.title('DESCRIPCION PRUEBA CAQ')
#plt.text(4, 1, t, ha='left', rotation=15, wrap=True)
##plt.text(6, 5, t, ha='left', rotation=15, wrap=True)
##plt.text(5, 5, t, ha='right', rotation=-15, wrap=True)
plt.text(5, 10, s=t, fontsize=7, style='oblique', ha='right',
         va='top')
#plt.text(3, 4, t, family='serif', style='italic', ha='right', wrap=True)
#plt.text(-1, 0, t, ha='left', rotation=-15, wrap=True)

plt.savefig("test", format='pdf')
