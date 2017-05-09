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
# python3 mut_rmsd.py 

# this script calculates the displacement between heavy atoms in mutant and wildtype 
# versions of the 3VKO protein

# files needed are 'wt.pdb' and 'mut.pdb', each of which has repulsive
# these are alighned files of 3VKO protein
# If the line in the pdb file contains coordinates it starts with Atom and has the following form
# col1 = "Atom"
# col2 = Atom serial number
# col3 = Atom Name
# col4 = Alternate location indicator
# col5 = Residue Name
# col6 = Chain Identifier
# col7 = Residue Sequence number
# col8 = Code for insertions of residues
# col9 = x coordinate (angstroms) 
# col10 = y coordinate (angstroms)
# col11 = z coordinate (angstroms)
# col12 = Atom element symbol




import numpy as np
import matplotlib.pyplot as plt
#from scipy.interpolate import griddata
#import matplotlib.cm as cm


#~~~~~~~~~~~~RMSD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f = open('mut.pdb', 'r')
#f.readline() # skip first line
# ~~initialize mutant parameters
#maNum = [] # mutant atom numbers
maName = [] # mutant atom names
#maltLocIndicator = [] # mutant alternative location indicator
#mrName = [] # mutant residue names
#mchainID = []
mrNum = [] # mutant residue Number
#insCode = []
mx = [] # mutant x, y and z
my = []
mz = []
maEl = [] # mutant element symbol

for line in f:  
    md = line.split() #mutant data
    #maNum.append(int(md[1]))
    maName.append(md[2])
    #mrName.append(md[3])
    mrNum.append(int(md[5]))
    mx.append(float(md[6]))
    my.append(float(md[7]))
    mz.append(float(md[8]))
    maEl.append(md[11])
f.close

isc = [i for i, x in enumerate(maName) if x != 'N' and x!='CA' and x!='C' and x!='O']# and x!='CB'] # all sidechain atoms
ind = [i for i, x in enumerate(mrNum) if x==35] # all atoms of mutation residue
iscr = [i for i, x in enumerate(ind) if x not in isc] # sidechain atoms of mutation residue
indd = np.delete(ind, iscr) # indices to remove from list for rmsd (these are the atoms that differ between ILE and PHE)
# remove the side chain atoms of the mutation site
#maNum = np.delete(maNum, indd)
maName = np.delete(maName, indd)
mrNum = np.delete(mrNum, indd)
#mrName = np.delete(mrName, indd)
maEl = np.delete(maEl, indd)
mx = np.delete(mx, indd)
my = np.delete(my, indd)
mz = np.delete(mz, indd)
# find indices of hydrogens and remove from lists
ind_H = [i for i, x in enumerate(maEl) if x == 'H']
maName = np.delete(maName, ind_H)
mrNum = np.delete(mrNum, ind_H)
mx = np.delete(mx, ind_H)
my = np.delete(my, ind_H)
mz = np.delete(mz, ind_H)


g = open('wt.pdb', 'r')
#f.readline() # skip first line
# ~~~~~~~~Initialize the wildtype parameters~~~~~~~~~~
waName = [] # atom Name
wrNum = [] # residue Number
wx = [] # atom coordinates
wy = []
wz = []
waEl = []

for line in g:  
    wd = line.split() #wild type data
    waName.append(wd[2])
    wrNum.append(int(wd[5]))
    wx.append(float(wd[6]))
    wy.append(float(wd[7]))
    wz.append(float(wd[8]))
    waEl.append(wd[11])
g.close

isc2 = [i for i, x in enumerate(waName) if x != 'N' and x!='CA' and x!='C' and x!='O']# and x!='CB'] # all sidechain atoms
ind2 = [i for i, x in enumerate(wrNum) if x==35] # all atoms of mutation residue
iscr2 = [i for i, x in enumerate(ind2) if x not in isc2] # sidechain atoms of mutation residue
indd2 = np.delete(ind2, iscr2) # indices to remove from list for rmsd (these are the atoms that differ between ILE and PHE)
# remove the side chain atoms of the mutation site
#maNum = np.delete(maNum, indd2)
waName = np.delete(waName, indd2)
wrNum = np.delete(wrNum, indd2)
#mrName = np.delete(mrName, indd2)
waEl = np.delete(waEl, indd2)
wx = np.delete(wx, indd2)
wy = np.delete(wy, indd2)
wz = np.delete(wz, indd2)
# find indices of hydrogens and remove from lists
ind_H2 = [i for i, x in enumerate(waEl) if x == 'H']
wx = np.delete(wx, ind_H2)
wy = np.delete(wy, ind_H2)
wz = np.delete(wz, ind_H2)

# Calculate rmsd for heavy atoms.
dx = np.zeros(len(mx))
dy = np.zeros(len(mx))
dz = np.zeros(len(mx))
rsq = np.zeros(len(mx))
for i in range(len(mx)):
    dx[i] = mx[i] - wx[i]
    dy[i] = my[i] - wy[i]
    dz[i] = mz[i] - wz[i]
    rsq[i] = dx[i]**2 + dy[i]**2 + dz[i]**2

rmsd = np.sqrt(sum(rsq)/len(rsq))
rsqn = rsq/len(rsq)
rootrsqn = np.sqrt(rsq)
print(rmsd)

# ~~~~~~~~~~~~~~~~~~ Plot the results ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
font = {'size':22}
plt.scatter(mrNum, rootrsqn, color='b')
plt.xticks(np.arange(0,175,25))
#plt.yticks(np.arange(-180,240,60))
plt.xlim(7,150)
plt.ylim(0,8)
plt.xlabel(r'Residue Number', **font) # spec latex
plt.ylabel(r'$d$ ($\AA$)', **font)
plt.title('Displacement of Heavy Atoms Between I35 and 135F',**font) 
plt.text(110,6.5, 'RMSD =' + '%.1f'% round(rmsd,3))#  '\n' 'Total number of entries = ' N '\n' 'Avg= 'avg   '\n'   'Standard Deviation = ' sigma)
#plt.show()

# residues of interest
mutSite = [36, 36]
mutLine = [0,10]
res138 = [138,138]
obs, = plt.plot(mutSite, mutLine, 'k--', linewidth=2, label='Mutation Site (Res 35)')
pred, = plt.plot(res138, mutLine, 'm--', linewidth=2, label='L138')
legend = plt.legend(handles=[obs,pred],loc=1)

plt.savefig('Displacement.png')
plt.close()


 
