# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:02:32 2016

@author: Hui
"""
#Write a python program to implement backsub and test your program
X=mat(" 6. 3. 9. 2.; 0. 4. 6. 1.; 0. 0. 8. 8.; 0. 0. 0. 5.")
y= mat("1.; 4.; 6.; 1.")
b=backsub(X,y)
b


#Write a python program to implement house and execute it
x= mat("1.4; 5.8; 2.3; 8.1; 9.0")
v=house(x)
v

#Write a python program to implement rowhouse and execute
X=mat("1.4 4.5 6.5; 5.8 3.2 7.3; 2.3 -2.6 8.2; 8.1 -5.8 -8.0; 9.0 0.3 1.5")
rowhouse(X,v)
