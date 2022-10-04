import xml.etree.ElementTree as ET

def FileCheck(inFile, outFile, var):
    try:
        tree = ET.parse(inFile)
        for desc in tree.findall(f'color[@name="{var}"]'):
            desc.text = "#2A2A2A"

        tree.write(outFile)
        return 1
    except IOError:
        print("Error: File does not appear to exist.")
        return 0

FileCheck("a.xml","b.xml","colorPrimary")