# HTMLtag to php function

## Principe

Script python qui parse les pages htm ou html dans différents repertoires pour remplacer les balise *img* par une fonction php *image*

Deux versions du programme :

* **imghtmltag2php_norespect.py** : utilisant la bibliothèque _BeautifulSoup_, mais réindente la page d'origine
* **imghtmltag2php.py** : parse ligne à ligne et respecte le ~~caca~~ code initial de la page.

## imghtmltag2php_norespect.py

Paramètre modifiable dans l'entête du script :

* **target_path** : liste de répertoire à analyser : **./** pour la racine **./MONREPERTOIRE/** pour mon repertoire
* **fileformat** : extension analysée

```python
target_path    = ['./file/']
fileformat     = 'html'
```

## imghtmltag2php.py

Étant donné que le parser est réalisé à la main, et par sousci de délai, les contraintes suivantes doivent être connu avant de prendre possession ~~du bolide~~ de l'outil :

1. Ne traite pas les multis attributs identiques (ne prend que la première valeur) et les valeurs d'attributs étant des noms d'attributs
2. Les attributs déclarés avec **'** (les attributs sont considérés comme étant déclarés avec **"** uniquement)

Paramètre modifiable dans l'entête du script :

* **paths** : liste de répertoire à analyser : ./ pour la racine ./MONREPERTOIRE/ pour le repertoire
* **extensions** : lites des extensions analysées
* **tag_search** : balise étudiée (écrite en minuscule)
* **php_fonction** : fonction php crée
* **tag_attributes** : liste des attributs analysées dans la balise étudiée

```python
paths            = ['./', './file/']
extensions       = ['html', 'htm']  
tag_search       = '<img'
php_fonction     = 'image'
tag_attributes   = ['src', 'class', 'title', 'alt', 'width', 'height']
```

### Remerciement

* La seule personne au monde qui sera capable de lire jusqu'à la fin de ce readme
* [`Beautiful Soup`](https://code.launchpad.net/~leonardr/beautifulsoup/bs4)  :  Bibliothèque Python d'analyse syntaxique de documents HTML et XML créée par Leonard Richardson
