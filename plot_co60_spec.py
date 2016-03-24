import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

mat.rcParams.update({'font.size': 14})
mat.rcParams.update({'font.family':'serif'})


#data = np.loadtxt('co60_spec')
data = np.loadtxt('unknown1')
#data  =np.loadtxt('unknown2')
#data = np.loadtxt('unknown1_271s')

energy = data[:,2]
counts = data[:,0]
uncertainty = data[:,1]

#plt.bar(energy,energy,alpha=0.1,color='b',yerr=uncertainty)

#plt.plot(energy,counts)
plt.errorbar(energy,counts,yerr=uncertainty,ecolor='g')

plt.xlabel('Energy ($keV$)')
plt.ylabel('Counts')

plt.show()







