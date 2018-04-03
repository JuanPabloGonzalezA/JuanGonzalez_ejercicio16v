import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt('datos.txt')
laminas=np.arange(1,len(datos)+1)
plt.plot(laminas,datos[:,0],label='# que tengo')
plt.plot(laminas,datos[:,1],label='# repetidas')
plt.legend()
plt.xlabel('# comprados')
plt.ylabel('#')
plt.savefig('grafica.png')
