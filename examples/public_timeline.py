#!/usr/bin/python
from identi import Identica
import json

identica = Identica()
pt_json = identica.getPublicTimeline()
j= pt_json[1:-1]

doll = "'" + str(j) +"'"
print doll.encode('utf-8')

a = json.loads(doll.encode('utf-8'))
#print type(doll)

#print a['text']
#print j['text']
