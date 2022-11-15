import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
    print("please specify input file")
    exit(1)

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for word in root:
    for x in word:
        for y in x:
            for z in y:
                print(z.attrib['word'], z.attrib['tag']
            print()
