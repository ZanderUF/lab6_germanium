import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat

mat.rcParams.update({'font.size': 14})
mat.rcParams.update({'font.family':'serif'})

data = np.loadtxt('energy_cal_data')

x=data[:,1]
y=data[:,0]

#x = [441.23,783.38,890]
#y = [662,1173,1333]

x_sp = np.linspace(0,1000)

m,b = np.polyfit(x,y,1)

plt.plot(x,y,'.')
plt.plot(x_sp, m*x_sp + b, '-')


plt.xlabel('Channel Number')
plt.ylabel('Energy $(keV)$')
print 'slope is',m
print 'y int is', b

plt.show()
