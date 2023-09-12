# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:58:28 2021

@author: Foza
"""
import math
def Fonction1(G0,Tau,Te):
    a = math.exp(- Te/Tau)
    x = G0*1 - a*G0
    return ("    {:.3f}\n--------------\n    (z - {:.3f}) ".format(x,a))
def Fonction2(G0,Tau,Te,n):
    a = math.exp(- Te/Tau)
    x = G0*1 - a*G0
    return ("{:.3f}.z^(-{:.3f})\n--------------------\n  (z - {:.3f}) ".format(x,n,a))
def Fonction3(Tau2,Tau1,Te):
    x1 = Te/Tau2 
    a1= math.exp(-x1)
    alpha = (Te/Tau1) - (Tau2/Tau1)*(1-a1)
    beta = (Tau2/Tau1)*(1-a1) - a1*(Te/Tau1)
    return ("({:.3f}.z + {:.3f})\n--------------------\n  (z - 1)(z - {:.3f}) ".format(alpha,beta,a1))
def Fonction4(G0,Tau1,Tau2,Te):
    x1 = Te/Tau1
    x2 = Te/Tau2
    a1 = math.exp(-x1)
    a2 = math.exp(-x2)
    alpha = G0*1 + G0*(a2*Tau2 - a1*Tau1)/(Tau1-Tau2)
    beta = G0*a1*a2 + G0*(a1*Tau2 - a2*Tau1)/(Tau1-Tau2)
    return ("({:.3f}.z + {:.3f})\n--------------------\n  (z - {:.3f})(z - {:.3f}) ".format(alpha,beta,a1,a2))
def Fonction5(G0,m,w0,Te):
    teta = w0*Te*(math.sqrt(1-m*m))
    x = m*w0*Te
    a0 = math.exp(-2*x)
    a1 = -2*math.exp(-x)*math.cos(teta)
    alpha = G0*1 - G0*math.exp(-x)*((m/(math.sqrt(1-m**2)))*math.sin(teta) + math.cos(teta))
    beta = G0*math.exp(-2*x) + G0*math.exp(-x)*((m/(math.sqrt(1-m**2)))*math.sin(teta) + math.cos(teta))
    return ("({:.3f}.z + {:.3f})\n--------------------\n  (z² + {:.3f}z + {:.3f}) ".format(alpha,beta,a1,a0))
def Fonction6(G0,Tau,Te):
    x = Te/Tau
    z0 = math.exp(-x)
    alpha = G0*(1 - z0)
    beta = G0*Te*z0
    return ("({:.3f})           {:.3f}(z - 1)\n--------------    -    ---------------------\n (z - {:.3f})      {:.3f}(z - {:.3f})²".format(alpha,beta,z0,Tau,z0))


    

