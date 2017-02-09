import xml.etree.ElementTree as ET


file = ET.parse('text.xml')
data = file.getroot()
checkIns = []
def pxml():
	for checkIn in data:
		checkIns.append(checkIn)
		print(checkIn.text)
pxml()
check = ET.SubElement(data, 'checkIn')
check.text = input()
pxml()
file.write('text.xml')
