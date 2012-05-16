#!/usr/bin/python
from identi import Identica

identica = Identica()

ut_xml = identica.getUserTimeline(screen_name="psibi")
statuses = identica.getValues(ut_xml,"text")

for value in statuses:
    print value
