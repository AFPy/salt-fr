Compte rendu Salt Meetup Paris - novembre 2014
==============================================


:date: 2014-12-11
:tags: cr, tinyclues, stats, ui, 
:category: Compte Rendus
:author: Arthur Lutz
:email: arthur.lutz@logilab.fr


La communauté Salt s'est a nouveau réunie pour son meetup bi-mestriel
autour de trois présentations. Voici un compte rendu (très court) pour
vous renvoyer vers les références.

Utilisation de salt pour gérer des machines desktop sous windows et mac os.
---------------------------------------------------------------------------

Aurélien Minet de l'`ENS  Cachan <http://www.ens-cachan.fr/>`_ nous a présenté son utilisation de salt dans la gestion de postes utilisateurs OS X et Windows. 

* OS X:

    * `Homebrew — The missing package manager for OS X <http://brew.sh/>`_

    * `salt.modules.brew <http://docs.saltstack.com/en/latest/ref/modules/all/salt.modules.brew.html>`_

    * `Homebrew Cask <http://caskroom.io/>`_

* Windows:

    * `salt.modules.win_*
      <http://docs.saltstack.com/en/latest/ref/modules/all/>`_

    * `salt.modules.chocolatey
      <http://docs.saltstack.com/en/latest/ref/modules/all/salt.modules.chocolatey.html#module-salt.modules.chocolatey>`_

    * `salt.modules.reg
      <http://docs.saltstack.com/en/latest/ref/modules/all/salt.modules.reg.html#module-salt.modules.reg>`_

    * pour chocolatey, possibilité d'héberger un repo sous linux avec
      `Simple Nuget
      <https://github.com/Daniel15/simple-nuget-server>`_

    * Mise en commun d'installeurs windows sous forme de states sur
      `salt-winrepo <https://github.com/saltstack/salt-winrepo>`_

`Support de sa présentation <./presentations/aminet-salt-macosx-win.pdf>`_

Création de statistiques  pour une infrastructure salt
------------------------------------------------------

Arthur Lutz de `Logilab <http://www.logilab.fr>`_ nous a présenté un
développement pour évaluer la distance entre l'état souhaité de son
infrastructure salt et l'état réel.

.. image:: ./images/salt-nov-2014-arthur.jpg
  :alt: Arthur Lutz

* `Support de présentation <http://slides.logilab.fr/salt-meetup-stats/>`_

* `Code sur bitbucket <https://bitbucket.org/arthurlogilab/salt-highstate-stats>`_

SaltPad
-------

.. image:: ./images/salt-nov-2014-boris.jpg
  :alt: Boris Feld

Boris Feld de `tinyclues <http://www.tinyclues.com/>`_ nous a présenté
une interface web pour piloter salt.

* `Slides <https://speakerdeck.com/lothiraldan/saltpad-the-web-gui-your-infrastructure-deserves>`_

* `Code sur github <https://github.com/tinyclues/saltpad>`_

Conclusion
----------

Merci à `tinyclues <http://www.tinyclues.com/>`_ d'avoir acceuilli et
apporté à boire, ainsi qu'à `Logilab <http://www.logilab.fr>`_ pour
les pizzas.

Pour le prochain meetup (en janvier), votez pour une date sur
`framadate <https://framadate.org/4cf63j6i23vbaeem>`_ et n'hésitez pas
à inscrire une proposition de présentation ou de lieu sur le `pad
d'organisation
<http://lite4.framapad.org/p/organisation-salt-meetups>`_.
