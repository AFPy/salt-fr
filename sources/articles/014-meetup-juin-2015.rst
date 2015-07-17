Compte rendu "Table ronde et Comparaison des frameworks" Salt Ansible Chef Puppet
=================================================================================

:date: 2015-07-17
:tags: compte rendu, puppet, chef,ansible, salt
:category: Compte Rendus
:author: Arthur Lutz
:email: arthur.lutz@logilab.fr

Comme `annoncé sur ce blog
<http://salt-fr.afpy.org/annonce-meetup-salt-table-ronde-et-comparaison-des-frameworks-salt-ansible-chef-puppet.html>`_,
le meetup de juin était un peu particulier. Nous avons rassemblé
plusieurs frameworks pour discuter comparativement des technologies
similaires à Salt. Nous sommes resortis avec une idée plus précise des
forces et faiblesses de chacun, mais aussi des idée pour améliorer
Salt.

Voici les `diapositives
<http://slides.com/arthurlogilab/meetup-salt-table-ronde-et-comparaison-des-frameworks-salt-ansible-chef-p-uppet#/>`_
pour introduire la soirée.

.. raw:: html
  
  <iframe
  src="//slides.com/arthurlogilab/meetup-salt-table-ronde-et-comparaison-des-frameworks-salt-ansible-chef-p-uppet/embed"
  width="576" height="420" scrolling="no" frameborder="0"
  webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Merci à Mathieu de `Bearstech <http://bearstech.com/>`_, Guilhem de
`Wemanity <http://wemanity.com/>`_, Francois de `D2SI
<http://d2-si.eu>`_ et Arthur de `Logilab <http://www.logilab.fr>`_
pour leurs interventions.

.. image:: ./images/compare_frameworks_salt_companies.png
  :alt: Puppet Salt Ansible Chef Logilab Bearstech Wemanity D2SI

Nous avons abordés 8 grandes thématiques : 

* Introduction intervenants et leurs boites

* Introduction générale par projet, historique, key features,
  languages de programmation, DSLs, installation multiplateforme
  (linux, unix, windows, mac, etc. ?)

* Déploiement de configuration et templating

* Executions de commandes,  organisation des noeuds, machines, ciblage

* Architecture (réseau, parefeux, bus de communication, protocoles) 

* Extensibilité, plugins, écriture et déploiement

* Orchestration, gestion de resources elastiques (cloud)

* Délegation, collaboration, environnemnts (dev,preprod, prod),
  approche Devops

* Composants "sur étagère", taille de la communauté, utilisateurs notables

* Offres "entreprise" autour ou écosystème commercial, Logique
  open-source / open-core, formations, livres

.. image:: ./images/salt-juin-2015.jpg
  :width: 600
  :alt: Meetup Salt juin 2015

Le meetup était visionnable en direct par streaming sur Dailymotion et
un montage de l'enregistrement a été publié par École42 :

.. raw:: html
  
  <iframe frameborder="0" width="560" height="315"
  src="//www.dailymotion.com/embed/video/x2xk20e"
  allowfullscreen></iframe><br /><a
  href="http://www.dailymotion.com/video/x2xk20e_conf-42-meetup-salt_tech"
  target="_blank">CONF@42 - MeetUp Salt</a> <i>par <a
  href="http://www.dailymotion.com/42Born2Code"
  target="_blank">42Born2Code</a></i>

Nous avons fini la soirée autour de pizzas et boissons offertes par
`Logilab <http://www.logilab.fr>`_. 

Lors de l'organisation (`sur le pad notamment
<https://lite5.framapad.org/p/organisation-comparaison-frameworks>`_)
, plusieurs personnes ont montré un interret pour ce type de débat,
notamment dans d'autres villes que Paris (Lyon, Rennes, Nantes),
n'hésitez pas à nous en parler sur `la liste de discussion
<http://lists.afpy.org/listinfo/salt-fr>`_ pour qu'on ré-itère
l'experience.
