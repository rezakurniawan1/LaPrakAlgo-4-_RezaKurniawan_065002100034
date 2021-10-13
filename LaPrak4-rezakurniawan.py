# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:22:17 2021

@author: Reza Kurniawan
"""
list = input("Masukkan list angka (integer): ")
list = list.split()

totalgenap = 0
for angka in list:
    if int(angka)%2 == 0:
        totalgenap += 1
        
if totalgenap > 0:
    print(f"List ini memiliki {totalgenap} angka genap")
else:
    print("List ini tidak memiliki angka genap")
