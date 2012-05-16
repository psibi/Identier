#!/usr/bin/python
from identi import Identica

identica = Identica()

status_xml = identica.showStatus(id="93506545")
status = identica.getValues(status_xml,"text")
print status[0]  #Since the List contains only one status.
