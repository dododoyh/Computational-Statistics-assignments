#1. Write multilinreg program in Matlab to solve the following regression problem: find least square estimate bˆ= argmin || y-Xb ||2
X=mat("5. 0. 9. 3.; 3. 6. 8. 9.; 4. 4. 9. 6.; 0. 3. 1. 8.; 2. 8. 2. 3.")
y= mat("20.; 17.; 32.; 10.;12.")
b=multilinreg(X,y)
b


#2. find and display the principal direction of a 2D dataset
pca_exp()
