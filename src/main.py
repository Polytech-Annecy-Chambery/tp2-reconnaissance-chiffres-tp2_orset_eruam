'''
File: main.py
Created Date: Friday August 27th 2021 - 02:35pm
Author: Ammar Mian
Contact: ammar.mian@univ-smb.fr
-----
Last Modified: Mon Aug 30 2021
Modified By: Ammar Mian
-----
Copyright (c) 2021 Université Savoie Mont-Blanc
'''
import matplotlib.pyplot as plt
from image import Image
from reconnaissance import reconnaissance_chiffre, lecture_modeles


if __name__ == '__main__':

    # Variables utiles
    path_to_assets = '../assets/'
    plt.ion() # Mode interactif de matplotlib our ne pas bloquer l'éxécutions lorsque l'on fait display
    
    #==============================================================================
    # Lecture image et affichage
    #==============================================================================
    image = Image()
    image.load(path_to_assets + 'test4.JPG')
    image.display("Exemple d'image")

    #==============================================================================
    # Binarisation de l'image et affichage
    #==============================================================================
    S = 70
    image_binarisee = image.binarisation(S)
    image_binarisee.display("Image binarisee")
    #==============================================================================
    # Localisation de l'image et affichage
    #==============================================================================
    image_localisee = image_binarisee.localisation()
    image_localisee.display("Image localisee")

    #==============================================================================
    # Redimensionnement de l'image et affichage
    #==============================================================================
    image_resizee = image_localisee.resize(100, 500)
    image_resizee.display("Image redimensionee")



    #==============================================================================
    # Lecture modeles et reconnaissance
    #==============================================================================
     
    
    liste_modeles = lecture_modeles(path_to_assets)
    """     img 1   """
    print("test1.JPG |`4")
    image.load(path_to_assets + 'test1.JPG')
    image.display("Exemple d'image")
    attendu = 4
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break
        
        
    """     img 2  """
    print("test2.JPG |`1")
    image.load(path_to_assets + 'test1.JPG')
    image.display("Exemple d'image")
    attendu = 1
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break

    """     img 3   """
    print("test3.JPG |`2")
    image.load(path_to_assets + 'test3.JPG')
    image.display("Exemple d'image")
    attendu = 2
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break


    """     img 4   """
    print("test4.JPG |`2")
    image.load(path_to_assets + 'test4.JPG')
    image.display("Exemple d'image")
    attendu =2
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break

    """     img 5   """
    print("test5.JPG |`2")
    image.load(path_to_assets + 'test5.JPG')
    image.display("Exemple d'image")
    attendu = 2
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break
        
    """     img 6  """
    print("test6.JPG |`4")
    image.load(path_to_assets + 'test6.JPG')
    image.display("Exemple d'image")
    attendu = 4
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            break
    """     img 7   """
    print("test7.JPG |`5")
    image.load(path_to_assets + 'test7.JPG')
    image.display("Exemple d'image")
    attendu = 5
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
            
            
    """     img 10   """
    print("test10.JPG |`6")
    image.load(path_to_assets + 'test10.JPG')
    image.display("Exemple d'image")
    attendu = 6
    i = 0
            
    a =False
    while i < 255:
        chiffre = reconnaissance_chiffre(image, liste_modeles, i)
        i += 1

           
        if chiffre == attendu and a ==False:
            print("S= " + str(i) + "| reconnu: " + str(chiffre))
            a = True
        elif chiffre != attendu and a ==True:
            print("*S= " + str(i) + "| reconnu: " + str(chiffre))
            a = False
        
    