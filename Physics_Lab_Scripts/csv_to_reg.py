#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:34:51 2017

@author: dmdixon
"""

import pandas as pd

def BS_Catalog_csv_to_reg(csv,inner_matching_ring,outer_matching_ring,maker=True):
        
    dataframe=pd.read_csv(csv)
            
    MWP_ID=dataframe['MWP ID']
    MWP_long=dataframe['MWP l']
    MWP_lati=dataframe['MWP b']
    MWP_hitrate=dataframe['hit rate']
    
    TwoMass_ID=dataframe['2Mass ID']
    TwoMass_long=dataframe['2Mass l']
    TwoMass_lati=dataframe['2Mass b']
    
    if maker == False: 
        filename = input('What is the full pathname of where you want to save the MWP region files?: ')
        MWP_file = open(filename,'w+')
    else:
        MWP_file=open(r'/Users/dmdixon/MilkyWayProject/Bow_Shock_Catalog/Regions/Current_MWP_BS.reg','w+')
        
    MWP_file.write("# Region file format: DS9 version 4.0")
    MWP_file.write("\n")
    MWP_file.write('global color=white')
    MWP_file.write("\n")
    MWP_file.write("\n")
    
    if maker == True:
        filename = input('What is the full pathname of where you want to save the 2MASS matched region files?: ')
        TwoMass_file = open(filename,'w+')
    else:
        TwoMass_file=open(r'/Users/dmdixon/MilkyWayProject/Bow_Shock_Catalog/Regions/Current_2MASS_BS.reg','w+')
    
    TwoMass_file.write("# Region file format: DS9 version 4.0")
    TwoMass_file.write("\n")
    TwoMass_file.write('global color=magenta')
    TwoMass_file.write("\n")
    TwoMass_file.write("\n")
    
    for n in range(len(dataframe)):     
        MWP_file.write(r' galactic;point (' + str(MWP_long[n])+r','+str(MWP_lati[n]) + r') # text={ID='+MWP_ID[n]+r' HR='+str(MWP_hitrate[n])+r'} point=cross size=10')
        MWP_file.write("\n")
        MWP_file.write(' galactic;circle (' + str(MWP_long[n])+','+str(MWP_lati[n]) +','+str(inner_matching_ring)+'"'+') #  point=circle 10')
        MWP_file.write("\n")  
        MWP_file.write(' galactic;circle (' + str(MWP_long[n])+','+str(MWP_lati[n]) +','+str(outer_matching_ring)+'"'+') #  point=circle 10')
        MWP_file.write("\n")  
        
        TwoMass_file.write(r' galactic;point (' + str(TwoMass_long[n])+r','+str(TwoMass_lati[n]) + r') # text={ID='+TwoMass_ID[n]+r'} point=cross size=10')
        TwoMass_file.write("\n")
        TwoMass_file.write(' galactic;circle (' + str(TwoMass_long[n])+','+str(TwoMass_lati[n]) +','+str(inner_matching_ring)+'"'+') #  point=circle 10')
        TwoMass_file.write("\n")  
        TwoMass_file.write(' galactic;circle (' + str(TwoMass_long[n])+','+str(TwoMass_lati[n]) +','+str(outer_matching_ring)+'"'+') #  point=circle 10')
        TwoMass_file.write("\n")  
        
    MWP_file.close
    TwoMass_file.close