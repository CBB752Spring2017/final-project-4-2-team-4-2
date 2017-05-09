---
layout: page
title: CBB752 Spring 2017
tagline: Final Project
---

Project Title
------------------


Table of Contents
-----------------------




**Contributors**
 -Writing:
 -Coding:
 -Pipeline: Krystle Reiss

### Introduction:





### Writing:








### Coding:


#### Documentation:
$ax+b$
\\[display\\]

#### Results:

![image](https://github.com/CBB752Spring2017/final-project-4-2-team-4-2-1/blob/master/wt4bmb.png)
![image](https://github.com/CBB752Spring2017/final-project-4-2-team-4-2-1/blob/master/mut4bmb.png)
![alt text](https://github.com/CBB752Spring2017/final-project-4-2-team-4-2-1/blob/master/distance.png)

![alt text](https://github.com/CBB752Spring2017/final-project-4-2-team-4-2-1/blob/master/overlayWhole.png)
![alt text](https://github.com/CBB752Spring2017/final-project-4-2-team-4-2-1/blob/master/res35zoom.png)





### Pipeline:
Multiple mutations at location 35 in chain A of protein 4BMB were evaluated using the Rosetta software package.

#### Documentation:
The protein structure 4BMB (Ruiz 2014) was acquired from the Protein Database. The Rosetta software package was used to create eleven
mutations at location 35 in chain A. These mutations were I35A, I35D, I35E, I35F, I35G, I35L, I35M, I35P, I35R, I35V, and I35Y. The
native protein and all mutations were optimized with Rosetta's Relax application (Nivón 2013) using the full atom and quick options. The
energies of these relaxed structures were calculated with Rosetta's Score application (O'Meara 2015), also using the full atom option.

#### Results:
Results were somewhat surprising. While the most and least stable mutation (valine and arginine, respectively) were predicatable, there 
were several unexpected results, such as the drastic energy differences between tyrosine and phenylalaline, the latter of which was very
unstable compared to the fore). It is thought that a slight shift in a nearby residue caused by the additonal hydroxyl group on tyrosine
was the cause for this disparity, although why this shift makes I35Y more stable than the native structure is unclear. The overlapping
structures of I35F and I35Y can be seen in 'I35YF_overlay.png'. I35F carbons are colored yellow and I35Y are pink. There was no overall
trend as to what made certain mutations more stable than others (e.g. size, hydrophobicity, charge), but some minor trends were present.
For example, residues that have sidechains that are three carbon long (glutamate and leucine) are more stabilizing while residues that
are shorter (alanine, aspartate, etc.) or longer (arginine and methionine) are less stable. The reason for this may be a pocket between 
V48 and I146 that is stabilized by when it is filled (as with glutamate and leucine). However, a residue that is too long, like 
arginine, clashes with the nearby residue F46.

#### Files:
Rosetta Score Output: score.sc

Scores with Differences: 4bmb_I35_mutation_scores.xlsx

Native Structure: 4bmb_0001.pdb

Mutant Structures: 4bmb.A-I32X_0001.pdb ('X' is replaced with the mutant amino acid's 1-letter abbreviation)

Images: I35X.png ('X' is replaced with the mutant amino acid's 1-letter abbreviation or omitted for native structure)

Overlay of I35Y and I35F: I35YF_overlay.png


#### References:
Nivón, L. G., Moretti, R., and Baker, D. (2013) A Pareto-Optimal Refinement Method for Protein Design Scaffolds. PLoS ONE 8.

O’Meara, M. J., Leaver-Fay, A., Tyka, M. D., Stein, A., Houlihan, K., Dimaio, F., Bradley, P., Kortemme, T., Baker, D., Snoeyink, J.,
 and Kuhlman, B. (2015) Combined Covalent-Electrostatic Model of Hydrogen Bonding Improves Structure Prediction with Rosetta. Journal of
 Chemical Theory and Computation 11, 609–622.
 
Ruiz, F. M., Scholz, B. A., Buzamet, E., Kopitz, J., André, S., Menéndez, M., Romero, A., Solís, D., and Gabius, H.-J. (2014) Natural 
 single amino acid polymorphism (F19Y) in human galectin-8: detection of structural alterations and increased growth-regulatory activity 
 on tumor cells. FEBS Journal 281, 1446–1464.








#### Conclusions:








#### References:

 References can be included here or at the end of each relevant section.
 
 
