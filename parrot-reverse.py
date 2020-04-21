from matplotlib.pyplot import *
from numpy import *

#ouverture du fichier image 
im1 = imread("./parrot.png")
#on crée une nouvelle image de même taille que image d'origine 
(l,c,t) = shape(im1)
im2 = zeros((l,c,t))

for i in range(l):          # on balaie toutes les lignes 
    im2[i] = flip (im1[i])
 
    for j in range(c):   
        sauv = im2[i,j,0]   
        im2[i,j,0] = im2[i,j,2]
        im2[i,j,2] = sauv
               
imshow(im2)
show(im2.any())               # on affiche l'image 2