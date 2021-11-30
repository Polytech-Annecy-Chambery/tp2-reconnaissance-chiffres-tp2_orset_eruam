from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        
        im_bin = Image()
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8)) #on créé une image vide 
        for l in range(self.H):
            for c in range(self.W):
                p = self.pixels[l][c] #on recupère la valeur du pixel de l'image "self"
                if p >= S:
                    im_bin.pixels[l][c] = 255  #on modifie le pixel de la nouvelle image en consequence
                else:
                    im_bin.pixels[l][c] = 0
    
        return im_bin
                

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        
        cmin = self.W-1 #on defini les valeurs initiales de cmin cmax lmin et lmax dans le pire des cas 
        cmax = 0
        lmin = self.H-1
        lmax = 0
        
        im_loc = Image()
        for l in range(self.H):
            for c in range(self.W):
                # lorsque l'on trouve un pixel de couleur, on verifie qu'il soit dans le carre formé par cmin|max et lmin-max, si besoin on agrandit le carre
                if self.pixels[l][c] == 0:
                    if l > lmax:
                        lmax = l
                    if l < lmin:
                        lmin = l
                    if c > cmax:
                        cmax = c
                    if c < cmin:
                        cmin = c
        #On gère le cas ou aucun pixel de couleur n'est trouvé                   
        if cmax - cmin <= 0:
            cmin = 0
            cmax = self.W-1
        if lmax - lmin <= 0:
            lmin = 0
            lmax = self.H-1

        im_loc.set_pixels(np.zeros((lmax-lmin, cmax-cmin), dtype=np.uint8))
        im_loc.set_pixels(self.pixels[lmin:lmax,cmin:cmax])
        return im_loc
               

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_res = Image()
        pixels_tab_res = resize(self.pixels, (new_H,new_W), 0)
        pixels_tab_res = np.uint8(pixels_tab_res*255)
        im_res.set_pixels(pixels_tab_res)
        
        return im_res
        



    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        nb_pix_sim = 0
        nb_pix = self.H * self.W
        sim = 0.0
        
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == im.pixels[l][c]:
                    nb_pix_sim += 1 
       
        sim = nb_pix_sim/nb_pix
        return sim 
    
                    
        
        
        

            

