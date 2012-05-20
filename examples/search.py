#!/usr/bin/python
from identi import Identica

identica = Identica()

result = identica.search(q="linux") #Returns a JSON output. Parse it as your need.
print result
