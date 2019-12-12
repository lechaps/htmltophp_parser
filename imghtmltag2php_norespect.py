# coding: utf8

import glob

from bs4 import BeautifulSoup

target_path    = ['./file/']
fileformat     = 'html'
status         = ''
for path in target_path:                                                #pour tous les dossiers à inspecter
    nbfile = 0
    print('**** Analyse du répertoire : '+path)
    path_file_list = glob.glob(path + '*'+fileformat )                  #recherche les fichiers du format considéré
    for path_file in path_file_list:                                    #pour tous les fichiers à inspecter
        print('**')
        with open(path_file, mode='r', encoding="utf8") as f :                  #ouverture du fichier en mode lecture
            file_content = f.read()                                             #lecture du fichier
            f.close()                                                           #fermeture du fichier (parce qu'on se respecte)
            soup = BeautifulSoup(file_content, 'html.parser')                   #parsing HTML du fichier
            for img in soup.find_all('img'):                                    #détection des balise <IMG>
                img.replace_with('<?php image("'+str(img.get("class"))+'", "'+str(img.get("src"))+'", , "'+str(img.get("alt"))+'", , "'+str(img.get("usemap"))+'", "'+str(img.get("height"))+'", "'+str(img.get("width"))+'"); ?>')
            nbfile+=1                                                           #comptage traiement
        new_file = open (path_file, mode='w', encoding="utf8")              #ouverture du fichier
        new_file.write(str(soup.prettify(formatter=None)))                  #ecrasement par nouveau contenu
        new_file.close()                                                    #fermeture du fichier (parce qu'on se respecte toujours!)  
    status+= (str(nbfile)+" fichiers parsés dans le repertoire "+path+"\n") #du log (parce qu'on est pas des bêtes)
print("Bilan : \n"+status)                                                  #bon bah on y va