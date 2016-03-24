import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat



mat.rcParams.update({'font.size': 14})
mat.rcParams.update({'font.family':'serif'})


data = np.loadtxt('eff_vs_energy')

x = data[:,0]
y = data[:,1]
yerr = data[:,2]

plt.errorbar(x,y, yerr=yerr,fmt='.')

#----------
plt.ylabel('Absolute Efficiency')
plt.xlabel('Energy ($keV$)')

plt.show()



