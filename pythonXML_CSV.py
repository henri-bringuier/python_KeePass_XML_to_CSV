import csv
from xml.etree import ElementTree
tree = ElementTree.parse('kp_bkp.xml')
root = tree.getroot()

for app in root.findall(".//History/.."):
    for subapp in app.findall("History"):
        app.remove(subapp)

tree.write('kp_purged.xml')

tree = ElementTree.parse('kp_purged.xml')
root = tree.getroot()

with open('kp.csv', 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    for entry in root.iter("Entry"):
        ligne=[]
        for subatt in entry.findall("String"):
            value = subatt.find('Value').text
            ligne=ligne+[value]
        writer.writerow(ligne)