from matplotlib.pyplot import *
from numpy import *

#ouverture du fichier image 
im1 = imread("./parrot.png")
#on crée une nouvelle image de même taille que image d'origine 
(l,c,t) = shape(im1)
im2 = zeros((l,c,t))

for i in range(l):          # on balaie toutes les lignes 
    im2[i] = flip(im1[i])
    for j in range(c):      # pour chaque ligne, on balaie toutes les colonnes
        val = (im1[i,j,0] + im1[i,j,1] + im1[i,j,2]) /3
        
        im2[i,j,0] = val   #R
        im2[i,j,1] = val   #V 
        im2[i,j,2] = val   #B
                
imshow(im2)
show(im2.any())               # on affiche l'image 2