Identier
---------

Identier is an Python API library for identi.ca.
``Identier`` provides a API for accessing services of identi.ca. This support various extensions provided by StatusNet apart from it's Twitter compatible API's.


Installation:
-------------

It is very easy to install Identier.

    	(pip install | easy_install) identi

... or in the traditional way:

    	$ git clone git://github.com/psibi/Identier.git
    	$ cd Identier
    	$ python setup.py install


Usage:
------

An example of how to get various status update from the public timeline.

    	from identi import Identica

    	identica = Identica()

    	pt_xml = identica.getPublicTimeline()
     	statuses = identica.getValues(pt_xml,"text") #List containing all statuses

    	for value in statuses:
    		print value

To Do:
-------
1. Write more examples for using this API inside the examples directory.
2. Remove Django dependency by providing alternate solution for solving Unicode related problem.
 
License:
--------
GNU General Public License v3 (GPLv3)

Bug Report:
-----------
Issue it here: https://github.com/psibi/Identier/issues


