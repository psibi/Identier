#!/usr/bin/python
from identi import Identica


identica = Identica()

pt_xml = identica.getPublicTimeline()
statuses = identica.getValues(pt_xml,"text")

for value in statuses:
    print value
