#!/usr/bin/python
# double underscores are for hidden/private/etc vars
__author__ = "Amber Jessop"
__copyright__ = "Copyright 2017"
__credits__ = ["Amber Jessop"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Amber Jessop"
__email__ = "amber.jessop@yale.edu"


# Usage: check files are in directory and run from command line:
# python3 mut_energy.py  
# files needed are 'Wildtype.txt' and 'Mutant.txt', each of which has repulsive 
# Lennard jones energies for side chain dihedral angle distribution
# first col: chi1
# second col: chi2
# third col: energy
# python3 mut_energy.py


import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import griddata
import matplotlib.cm as cm


wt_data = np.genfromtxt('Wildtype.txt', skip_header=0)
#wt_data = np.genfromtxt('4BMB_I35.txt', skip_header=0)
#f.readline() # skip first line
wt_chi1 = wt_data[:,0]
wt_chi2 = wt_data[:,1]
wt_E = wt_data[:,2]

wt_chi1 = np.unique(wt_chi1)
wt_chi2 = np.unique(wt_chi2)
Wchi1, Wchi2 = np.meshgrid(wt_chi1, wt_chi2)
W_E = wt_E.reshape(len(wt_chi2),len(wt_chi1))
CS = plt.contourf(Wchi1, Wchi2, W_E, 50, cmap = plt.cm.hot, vmin = -0.5, vmax = 1)
plt.colorbar()
plt.show()

font = {'size':22}
plt.xticks(np.arange(0,420,60))
plt.yticks(np.arange(0,420,60))
plt.xlim(0,360)
plt.ylim(0,360)
plt.xlabel(r'$\chi_1$ ($^{\circ}$)', **font) # spec latex
plt.ylabel(r'$\chi_2$ ($^{\circ}$)', **font)
plt.title('Wildtype 4BMB I35',**font) 
plt.savefig('wt4bmb.png')
plt.close()


mt_data = np.genfromtxt('Mutant.txt', skip_header=0)
mt_chi1 = mt_data[:,0]
mt_chi2 = mt_data[:,1]
mt_E = mt_data[:,2]


mt_chi1 = np.unique(mt_chi1)
mt_chi2 = np.unique(mt_chi2)
Mchi1, Mchi2 = np.meshgrid(mt_chi1, mt_chi2)
M_E = mt_E.reshape(len(mt_chi2),len(mt_chi1))
CS = plt.contourf(Mchi1, Mchi2, M_E, 50, cmap = plt.cm.hot, vmin = 133, vmax = 150)
plt.colorbar()
plt.show()

font = {'size':22}
plt.xticks(np.arange(0,420,60))
plt.yticks(np.arange(0,420,60))
plt.xlim(0,360)
plt.ylim(0,360)
plt.xlabel(r'$\chi_1$ ($^{\circ}$)', **font) # spec latex
plt.ylabel(r'$\chi_2$ ($^{\circ}$)', **font)
plt.title('Mutant 4BMB I35F',**font) 
plt.savefig('mut4bmb.png')
plt.close()


 
