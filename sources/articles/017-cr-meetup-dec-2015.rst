Compte rendu (sommaire) du meetup Salt Paris de décembre 2015
=============================================================

:date: 2016-01-20
:tags: supervision, web, saltpad, logilab, tinyclues, canal+
:category: Compte Rendus
:author: Arthur Lutz
:email: arthur.lutz@logilab.fr


Le jeudi 17 decembre 2015, `comme annoncé
<http://salt-fr.afpy.org/annonce-meetup-salt-decembre-2015.html>`_,
une partie de la communauté Salt s'est réuni autour de trois
présentation dans les locaux de Vivendi / Canal+.

**Retour d'expérience : Un peu de sel pour être HAPI - Metin OSMAN (Canal+)**

Metin Osman nous a présenté un retour d’expérience sur l'utilisation
de Salt à Canal+ avec un peu de fabric, jenkins, git et des syndics
Salt (mais aussi elasticsearch, logstash, redis, nginx,
etc.). Prochainement ils espèrent utiliser gitfs et docker. La
présentation est `disponible sur slideshare
<http://www.slideshare.net/plusdedev/un-peu-de-sel-pour-tre-hapi>`_.
  
.. raw:: html 

    <iframe src="//www.slideshare.net/slideshow/embed_code/key/5gvdhLfqjWYoya" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/plusdedev/un-peu-de-sel-pour-tre-hapi" title="Un peu de sel pour être HAPI" target="_blank">Un peu de sel pour être HAPI</a> </strong> from <strong><a href="//www.slideshare.net/plusdedev" target="_blank">Canal+ Dev</a></strong> </div>

**La supervision pilotée par Salt avec carbon/graphite/grafana -  Arthur Lutz (Logilab)**


.. image:: https://pbs.twimg.com/media/CWcuTcyW4AAr7bZ.jpg
	   :alt: Salt Meetup 

Arthur Lutz a présenté une démo dans des docker (lancés par
`docker-compose <https://docs.docker.com/compose/>`_) en montant une
architecture frontal+application+base de données et en supervisant le
tout avec Salt. Les résultats de la supervision sont stockés dans un
graphite (bases temporelles whisper) et des tableaux de bord sont
construits en utilisant `grafana <http://grafana.org/>`_. La démo est
disponible dans un dépôt mercurial sur `bitbucket
(salt_graphite_grafana)
<https://bitbucket.org/arthurlogilab/salt_graphite_grafana/>`_. Quelques
`slides <http://slides.logilab.fr/2015/salted_graphite_grafana/>`_
pour introduire le tout sont aussi publiés.

.. image:: https://bytebucket.org/arthurlogilab/salt_graphite_grafana/raw/0474047592e3c65f683792543be24f0370da8f73/Screenshot.png
	   :alt: Salt + Graphite + Grafana

.. https://twitter.com/douardda/status/677560204343549953

**Une interface web open-source pour Salt avec SaltPad v.2 en ReactJS - Boris Feld (tinyclues)**

Boris a présenté la nouvelle version de SaltPad en `ReactJS
<http://facebook.github.io/react/>`_ (la précédente version était en
`Flask <http://flask.pocoo.org/>`_)
https://github.com/tinyclues/saltpad/

.. image:: https://github.com/tinyclues/saltpad/raw/master/screenshots/highstate_result.png
	   :alt: Saltpad screenshot

Nous aurons peut-être, dans les prochaines semaines, une vidéo montée
par `Julien <https://twitter.com/Djiit>`_ de Canal+.

Merci à Canal+ / Vivendi pour le lieu. Merci à `Logilab
<http://www.logilab.fr>`_ pour les pizzas & bières.

La suite : un meetup en février ?

