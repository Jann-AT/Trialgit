# -*- coding: utf-8 -*-
"""
Created on Sun May 12 01:08:19 2024

@author: Samurai
"""

# 1st input: enter height in meters e.g: 1.65
#height = input()
height = input("What is your height?\n")
# 2nd input: enter weight in kilograms e.g: 72
#weight = input()
weight = input("What is your weight?\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

#BMI=weight_as_int/height_as_float**2
BMI=weight_as_int/(height_as_float*height_as_float)

print(int(BMI))