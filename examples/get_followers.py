#!/usr/bin/python
from identi import Identica

identica = Identica()

gt_xml = identica.getFollowersStatus(screen_name="psibi")
statuses = identica.getValues(gt_xml,"text")

for value in statuses:
    print value
