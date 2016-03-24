import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

mat.rcParams.update({'font.size': 14})
mat.rcParams.update({'font.family':'serif'})

data_eff = np.loadtxt('abs_eff')

x = data_eff[:,0]
y = data_eff[:,1]

plt.plot(x,y,'.')

plt.ylabel('Absolute Efficiency ($\%$)')
plt.xlabel('Energy $(keV)$')

plt.show()
