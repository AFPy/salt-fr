Compte rendu Salt Meetup Paris - octobre 2015
==============================================

:date: 2015-10-08
:tags: compte rendu, salt, gpg, peer-publish
:category: Compte Rendus
:author: Paul Tonelli
:email: tonelli@heuritech.com

Les utilisateurs de salt parisiens ont à nouveau frappé, accueillis chez
Weborama_ avec des pizzas offertes par Heuritech_. Nous avons pu discuter
tranquillement de:

.. _Weborama: http://www.weborama.com/fr/
.. _Heuritech: http://www.heuritech.com/

* Chiffrage au sein des fichiers salt, présenté par Ronan Amicel (`Pocket
  Sensei`_): plutôt que de devoir sécuriser l'intégralité d'un dépot il est
  possible d'ajouter au sein des fichiers sls salt des blocs de texte chiffrés
  par gpg_. Ces blocs sont ensuites décodés à la volée par un `renderer gpg
  <https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html>`_,
  ajouté à la suite des renderer yaml et jinja2 sur le master. Seul le master
  doit donc avoir accès à la clé privée.

.. _`Pocket Sensei`: http://www.pocketsensei.fr/
.. _GPG: https://www.gnupg.org/

* L'utilisation de peer publish dans Salt par Damien Desmaret (Weborama_). Le
  `peer-publish`_ est un des moyens qui permet à des minions de lancer des
  opérations ou de récupérer des informations sur d'autres minions. Cela permet
  par exemple de mettre à jour les listes de pairs sur un cluster lors de
  l'ajout d'une machine. La suite avec le réactor lors d'un prochain meetup.

.. _`peer-publish`: https://docs.saltstack.com/en/latest/ref/peer.html

.. image:: ./images/salt-oct-2015.jpg
  :width: 600
  :alt: Meetup Salt octobre 2015


N'hésitez pas à en parler sur `la liste de discussion
<http://lists.afpy.org/listinfo/salt-fr>`_.
