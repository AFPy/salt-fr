Le blog de la communauté Salt-fr, propulsé par `Pelican <http://docs.getpelican.com/>`_.

* `Blog <http://salt-fr.afpy.org>`_
* `Repos Github <https://github.com/AFPy/salt-fr>`_
* `Build Travis <https://travis-ci.org/AFPy/salt-fr>`_

Écrire un article
##################

* Il suffit de le rédiger dans un fichier ``sources/00X-article.rst``
  en suivant les exemples existants (metadata)

* L'ajout du fichier dans le repos sur la branche master relancera
  automatiquement le déploiement du blog en statique

Générer le blog en local
#########################

* Forker/Cloner le dépôt

* Adapter un fichier de settings ``localsettings.py`` à partir de
  ``localsetting.py.sample``

* Lancer la génération du blog en local : ``pelican -s
  localsettings.py`` et ``make serve``

Organisation collaborative
##########################

Le framapad suivant est diponible pour toute remarque ou idée
concernant les futurs meetups, le blog, ou autre: `le pad
<http://lite4.framapad.org/p/organisation-salt-meetups>`_.

Merci aux contributeurs de https://github.com/AFPy/python-nantes/ dont
ce projet est *très* largement inspiré (un fork en fait).



