# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:13:47 2020

@author: dverhoeff
"""

import os
import math
import matplotlib.pyplot as plt

def ratio_calc(inch):   
    try:
        ratio_in=input('Aspect ratio?\n'
                       '(Common ratios: '
                       '4:3, 5:4, 16:9, 16:10)\n\n')
                
        ratio=float(ratio_in.rpartition(':')[2])/float(ratio_in.rpartition(':')[0])
           
        cm=float(inch)*2.54       
        theta_rad=math.atan(ratio)
        theta_deg=theta_rad*180/math.pi
        
        width=math.cos(theta_rad)*cm*10
        height=math.sin(theta_rad)*cm*10
        
        plt.plot(width, height)
        plt.plot([0, width], [0, height], 'r')
        plt.text(width*0.5, height*0.5, '%s inch' %(inch), fontsize=15,  color='red', 
                 rotation = theta_deg,  horizontalalignment='center', verticalalignment='center', backgroundcolor='w')
        plt.title('Aspect ratio: %s' %(ratio_in), size = 15)
        plt.xlabel('{:.3f} mm'.format(width), size = 15)
        plt.ylabel('{:.3f} mm'.format(height), size = 15)
        plt.axis('scaled')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        
        print()
        os.system("pause")
    except:
        print('Invalid input!\n')
        os.system("pause")
        
inch=input('Screen diagonal in inches?\n')

try:
    val = int(inch)
    ratio_calc(inch)
except ValueError:
    try:
        val = float(inch)
        ratio_calc(inch)
    except ValueError:
        print('Invalid input!\n')
        os.system("pause")

