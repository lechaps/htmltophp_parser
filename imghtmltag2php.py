# coding: utf8

import glob

# P A R A M E T R E   D U   T R A I T E M E N T 
paths            = ['./', './file/']                                        #liste de répertoire à analyser : ./ pour la racine ./MONREPERTOIRE/ pour le repertoire
extensions       = ['html', 'htm']                                          #lites des extensions analysées
tag_search       = '<img'                                                   #balise étudiée (écrite en minuscule)
php_fonction     = 'image'                                                  #fonction php
tag_attributes   = ['src', 'class', 'title', 'alt', 'width', 'height']      #liste des attributs analysées dans la balise étudiée

# E N   D E S S O U S   D ' I C I ,   C E L U I   Q U I   M O D I F I E ,   C ' E S T   C E L U I   Q U I   A S S U M E
nb_file_global   = 0        #compteur du nombre de fichier scannés par le script
nb_tag           = 0        #compteur du nombre de tag traité par le script
# P O U R   T O U S   L E S   D O S S I E R S   A   I N S P E C T E R
for path in paths:                
    print('> Répertoire : '+path)
    nb_file_directory = 0       #compteur du nombre de fichier du repertoire
    # P O U R   T O U T E S   L E S   E X T E N S I O N S   A   I N S P E C T E R 
    for extension in extensions:     
        print('>> Extension : '+extension)
        nb_file_extension = 0       #compteur du nombre de fichier de l'extension
        files = glob.glob(path + '*'+extension)    #recherche les fichiers avec l'extension considérée
        #P O U R   T O U S   L E S   F I C H I E R S   D U   R E P E R T O I R E   A V E C   L ' E X T E N S I O N   R E C H E R C H É E
        for file in files:                    
            print('>>> Fichier : '+file)                   
            nb_tag_file=0        #compteur du nombre de tag trouvé dans un fichier
            with open(file, mode='r', encoding="utf8") as stream :   #ouverture du fichier en mode lecture
                content = []    #contenu final du fichier
                line_number=0   #compteur de ligne du fichier
                # P O U R   T O U T E S   L E S   L I G N E S   D U   F I C H I E R 
                for line in stream: 
                    line_number+=1  
                    read = line.lower()     #le contenu est minisculé (ok, le mot n'existe pas mais on se comprend!)                                
                    write= ''
                    tag  = ''
                    # R E C H E R C H E  D E   L A   P R E S E N C E   D E   P L U S I E U R S   T A G   D A N S   L A   L I G N E
                    while tag_search in read:
                        before = read[:read.index(tag_search)]      #chaine précédent le tag
                        try:
                            nb_tag_file+=1
                            nb_tag+=1
                            tag = read[read.index(tag_search):read.index('>', read.index(tag_search))+1]    #chaine représentant la balise HTML étudiée
                            read = read[read.index('>', read.index(tag_search))+1:]                         #le reste de la ligne reste à analyser
                            php_str = '<?php '+php_fonction+'('     #déclaration de la fonction php
                            #P O U R   T O U S   L E S   A T T R I B U T S   E X A M I N É S 
                            for attribute in tag_attributes:
                                try:
                                    value=tag[tag.index('"', tag.index(attribute))+1:tag.index('"', tag.index('"', tag.index(attribute))+1)]  #valeur de l'attribut
                                    php_str+='\''+value.strip()+'\', '  
                                except:
                                    php_str+='null, '
                            php_str=php_str[:len(php_str)-2]    #construction de la fonction php
                            php_str+='); ?>'                 
                            write = write+before+php_str    #construction de la ligne écrite dans le fichier
                        except:
                            write = write+read               #construction de la ligne écrite dans le fichier
                            read = ''
                            print('     # W A R N I N G : non respect HTML (> non trouvé) à la ligne '+str(line_number)+' : '+write.strip())
                    write+=read
                    content.append(write)       #écriture de la ligne dans le fichier
            stream.close()       #fermeture du fichier (par qu'on se respecte)
            with open(file, mode='w', encoding="utf8") as stream:       #ouverture du fichier en mode écriture
                stream.writelines(content)
            stream.close()      #fermeture du fichier (par qu'on se respecte...toujours)
            nb_file_extension+=1
            nb_file_global+=1
            nb_file_directory+=1
            print ('>>> '+str(nb_tag_file) + ' '+tag_search+'> traités')
        print ('>> '+str(nb_file_extension) + ' fichiers '+extension+' scannés dans le repertoire '+path)
    print ('> '+str(nb_file_directory) + ' fichiers scannés dans le repertoire '+path)
print ("T O T A L  S C R I P T : " + str(nb_file_global) + ' fichiers scannés / '+str(nb_tag)+" tags remplacés")
