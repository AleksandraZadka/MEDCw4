'''
Created on 1 lut 2015

@author: Alex
'''
#!/usr/bin/env python
#-*- coding: utf-8 -*-



from math import sqrt
from numpy import corrcoef
users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0
    klucze1=rating1.keys()
    klucze2=rating2.keys()
    wartosci1=rating1.values()
    wartosci2=rating2.values()
    iloczyn=0
    sumax=0
    sumay=0
    sumax2=0
    sumay2=0
    
    for i in xrange(0, len(wartosci1)):       
        iloczyn=iloczyn+wartosci1[i]*wartosci2[i]  
        sumax=sumax+wartosci1[i]
        sumay=sumay+wartosci2[i]
        sumax2=sumax2+wartosci1[i]**2
        sumay2=sumay2+wartosci2[i]**2
    korelacja=(iloczyn-((sumax*sumay)/len(wartosci1)))/(sqrt(sumax2-(sumax**2/len(wartosci1)))*sqrt(sumay2-(sumay**2/len(wartosci2))))    
    return korelacja

print pearson(users["Ania"],users["Bonia"])

def pearsonNumpy(rating1, rating2):
    
    korelacja=0
    poszkorel=corrcoef(rating1.values(), rating2.values())
    print poszkorel[1,0]
    korelacja=poszkorel[1,0]
    return korelacja

print pearsonNumpy(users["Ania"],users["Bonia"])