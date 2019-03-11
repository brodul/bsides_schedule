import xml

import pyaml
import xml.etree.ElementTree as ET

tree = ET.parse('schedule.xml')
root = tree.getroot()
day = root.find('day')

rooms = ('Living room', 'Back room')
for room in rooms:
    day.append(ET.Element('day', text=room))


import pdb; pdb.set_trace()
print(root)