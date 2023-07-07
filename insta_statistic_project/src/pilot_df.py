#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:16:13 2023

@author: seanyoo
"""
import pandas as pd 


multigp_df= pd.read_csv('/Users/seanyoo/Desktop/FPV_PILOT_DF/pilot_df/Multigp.csv')
mldr_df = pd.read_csv('/Users/seanyoo/Desktop/FPV_PILOT_DF/pilot_df/MLDR.csv')
bdra_df= pd.read_csv('/Users/seanyoo/Desktop/FPV_PILOT_DF/pilot_df/BDRA.csv')
dcl_df= pd.read_csv('/Users/seanyoo/Desktop/FPV_PILOT_DF/pilot_df/DCL.csv')

mldr_df = mldr_df.rename(columns = {"Handle":"Name"})
mldr_df = mldr_df.rename(columns=lambda x: x.capitalize())
mldr_df.columns = mldr_df.columns.str.strip()
mldr_df = mldr_df[["Name","Type of pilot","Youtube", "Instagram"]]

bdra_df = bdra_df.rename(columns=lambda x: x.capitalize())
bdra_df = bdra_df[["Name","Type of pilot","Youtube", "Instagram"]]

dcl_df =dcl_df.rename(columns={"Type of Pilot" : "Type of pilot"})
dcl_df = dcl_df[["Name","Type of pilot","Youtube","Instagram"]]

multigp_df = multigp_df.rename(columns= {"Type of Pilot" : "Type of pilot"})
multigp_df = multigp_df[["Name","Type of pilot","Youtube", "Instagram"]]

df = pd.concat([multigp_df, dcl_df, bdra_df,mldr_df], ignore_index=True, sort=False)


df

#convert to xlsx
#df.to_excel(r'C:\Users\seanyoo\Desktop\pilot_df.xlsx', index=False)

#convert to csv
#df.to_csv('pilot_df.csv', index=False)