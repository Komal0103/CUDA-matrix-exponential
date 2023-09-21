# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:57:47 2023

@author: yesh
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:43:30 2022

@author: yesh
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:22:15 2022

@author: yesh
"""
import multiprocessing as mp
import numpy as np
import time
#from Recom_yield import *
from qutip import *
import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
import math as mt
__author__ = 'Yash Tiwari'
import os
import xlsxwriter
from scipy.linalg import expm, sinm, cosm
import cmath
import scipy as sc

from itertools import starmap

par=1.7609*10**11; #mub(eV)/
B0=50*10**-6 # Geomagnetic field in Frankfurt (Tesla)
theta=0;
phi=0;
pi=mt.pi;
kf=10**6;
kb=10**6;
u=0;
knoise=10**4;
D=0


   
times = np.linspace(0, 10*10**-6, 10000)
noe_times=len(times)

#########################spin 1 operator############
Ix=np.array([[0,1,0],[1,0,1],[0,1,0]])
Ix=1/mt.sqrt(2)*(Ix)
Ixq=Qobj(Ix)
        
Iy=np.array([[0,-1.0j,0],[1.0j,0,-1.0j],[0,1.0j,0]])
Iy=1/mt.sqrt(2)*(Iy)
Iyq=Qobj(Iy)
        
Iz=np.array([[1,0,0],[0,0,0],[0,0,-1]])
Iz=(Iz)
Izq=Qobj(Iz)

sx=0.5*sigmax();
sy=0.5*sigmay();
sz=0.5*sigmaz();


#########################Hyperfine parmeter############
        
FN_5=np.array([[-0.0994543,0.002869,0],[0.002869,-0.087455,0],[0,0,1.7569]])*10**-3;
#FN_10=np.array([[-0.0148798,-0.00205738,0],[-0.00205738,-0.0236651,0],[0,0,0.60458]])*10**-3;
        
WN_1=np.array([[-0.0529384,0.0586559,-0.0460243],[0.0586559,0.564457,-0.564786],[-0.0460243,-0.564786,1.053143]])*10**-3;
#WH_1=np.array([[-1.70098,0.206185,0.0193279],[0.206185,-0.041571,0.307287],[0.0193279,0.307287,-0.352472]])*10**-3;



s1x=tensor(sx,qeye(2),qeye(3),qeye(3))
s1y=tensor(sy,qeye(2),qeye(3),qeye(3))
s1z=tensor(sz,qeye(2),qeye(3),qeye(3))
      
      
      
s2x=tensor(qeye(2),sx,qeye(3),qeye(3))
s2y=tensor(qeye(2),sy,qeye(3),qeye(3))
s2z=tensor(qeye(2),sz,qeye(3),qeye(3))

#########################HPERFIEN########################################

        
FN_5_hfi = (FN_5[0][0])*tensor(sx,qeye(2),Ixq,qeye(3))+  \
           (FN_5[0][1])*tensor(sy,qeye(2),Ixq,qeye(3))+  \
           (FN_5[0][2])*tensor(sz,qeye(2),Ixq,qeye(3))+  \
           (FN_5[1][0])*tensor(sx,qeye(2),Iyq,qeye(3))+  \
           (FN_5[1][1])*tensor(sy,qeye(2),Iyq,qeye(3))+  \
           (FN_5[1][2])*tensor(sz,qeye(2),Iyq,qeye(3))+  \
           (FN_5[2][0])*tensor(sx,qeye(2),Izq,qeye(3))+  \
           (FN_5[2][1])*tensor(sy,qeye(2),Izq,qeye(3))+  \
           (FN_5[2][2])*tensor(sz,qeye(2),Izq,qeye(3)); 

    


WN_1_hfi = (WN_1[0][0])*tensor(qeye(2),sx,qeye(3),Ixq)+  \
           (WN_1[0][1])*tensor(qeye(2),sy,qeye(3),Ixq)+  \
           (WN_1[0][2])*tensor(qeye(2),sz,qeye(3),Ixq)+  \
           (WN_1[1][0])*tensor(qeye(2),sx,qeye(3),Iyq)+  \
           (WN_1[1][1])*tensor(qeye(2),sy,qeye(3),Iyq)+  \
           (WN_1[1][2])*tensor(qeye(2),sz,qeye(3),Iyq)+  \
           (WN_1[2][0])*tensor(qeye(2),sx,qeye(3),Izq)+  \
           (WN_1[2][1])*tensor(qeye(2),sy,qeye(3),Izq)+  \
           (WN_1[2][2])*tensor(qeye(2),sz,qeye(3),Izq); 



H_hi_t=FN_5_hfi+WN_1_hfi;
H_total_hfi = par*(H_hi_t);


################################################################


dithe = (0.25)*pi;
diphi = (0)*pi;




H_x_zeeman = par*B0*((s1x +s2x) * mt.sin(theta) *  mt.cos(phi)) 
H_y_zeeman = par*B0*( (s1y +s2y) *  mt.sin(theta) * mt. sin(phi)) 
H_z_zeeman = par*B0*((s1z +s2z)* mt.cos(theta))

H_total_zeeman =  H_x_zeeman + H_y_zeeman + H_z_zeeman

    #Hamiltonian Hyperfine

    #First pair


F_x = tensor(sx,qeye(2)) + tensor(qeye(2),sx);
F_y = tensor(sy,qeye(2)) + tensor(qeye(2),sy);
F_z = tensor(sz,qeye(2)) + tensor(qeye(2),sz);



D=-(0)*par
H1_D=(2/3)*D*(-tensor(sx,sx)-tensor(sy,sy)+2*tensor(sz,sz))
vx1=(-1.0j*F_z*diphi).expm()*((-1.0j*F_y*dithe).expm())*H1_D*((1.0j*F_y*dithe).expm())*((1.0j*F_z*diphi).expm())
H1_Df = tensor(vx1,qeye(3),qeye(3));

    #fig,g2 = plt.subplots(figsize=(10,7)) 
tr=[];


HTotal=H_total_zeeman+H_total_hfi+H1_Df;


P_C=[[0 for x in range(4)] for x in range(4)]
P_C[1][1]=0.5*(1 - mt.sin(u))
P_C[1][2]=-0.5*mt.cos(u)
P_C[2][1]=-0.5*mt.cos(u)
P_C[2][2]=0.5*(1 + mt.sin(u))
P_CQ=Qobj(P_C);
P_Cr=tensor(P_CQ,qeye(3),qeye(3));
P_Cr.dims=[[2, 2, 3, 3], [2, 2, 3, 3]]

P_Crr = (-1.0j*diphi*(s1z + s2z)).expm()*(-1.0j*dithe*(s1y + s2y)).expm()*P_Cr*(1.0j*dithe*(s1y + s2y)).expm()*(1.0j*diphi*(s1z + s2z)).expm();

Chem_reaction=0.5*(kb*P_Crr + kf*tensor(qeye(2),qeye(2),qeye(3),qeye(3)));


Final=HTotal-1.0j*Chem_reaction     ##FINAL HAMILTONIAN
     
    ###########################################################################


P_I=[[0 for x in range(4)] for x in range(4)]
P_I[1][1]=0.5*(1 + mt.sin(u))
P_I[1][2]=-0.5*mt.cos(u)
P_I[2][1]=-0.5*mt.cos(u)
P_I[2][2]=0.5*(1 - mt.sin(u))
P_IQ=Qobj(P_I);
Projection=P_IQ;
Projection.dims=[[2,2], [2,2]]
P_Ir=tensor(P_IQ,qeye(3),qeye(3));
P_Ir.dims=[[2, 2, 3, 3], [2, 2, 3, 3]]


P_Irr = (-1.0j*diphi*(s1z + s2z)).expm()*(-1.0j*dithe*(s1y + s2y)).expm()*P_Ir*(1.0j*dithe*(s1y + s2y)).expm()*(1.0j*diphi*(s1z + s2z)).expm();
    ###########################################################################INITIAL STATE############################
krate=mt.sqrt(knoise)
N1=krate*s1x;
N2=krate*s1y;
N3=krate*s1z;
N4=krate*s2x;
N5=krate*s2y;
N6=krate*s2z;
Noise=[N1,N2,N3,N4,N5,N6];

    ##################################################
tr1=[];

P_Irr=P_Irr/9;
def Hy_coeff(t, args):
    return -1 * np.sin(-2*resonant_frequency[0]*t );

options = qutip.Options(normalize_output=False)
#result = mesolve(-1.0j*(spre(Final)-spost(Final).dag()),P_Irr, times, Noise,[], options=options)
H=-1.0j*(spre(Final)-spost(Final).dag())
result = mesolve(H,P_Irr, times, [],[], options=options)
x12=result.states

for t1 in range(0,noe_times):
      rh=x12[t1]
      rhf=rh*P_Crr;
         #r1=rh.ptrace([0,1])
         #tr.append(expect(Projection.unit(),r1));
      tr1.append(rhf.tr())
        
    #g2.plot(times, tr)
    #g2.grid()


result=abs(-1*kb*np.trapz(times,tr1))
print(result)