import xml.etree.ElementTree as ET
import sys

def FileChange(inFile, outFile, var, color):
    try:
        tree = ET.parse(inFile)
        for desc in tree.findall(f'color[@name="{var}"]'):
            desc.text = f'#{color}'

        tree.write(outFile)
        return 1
    except IOError:
        print("Error: File does not appear to exist.")
        return 0


param = sys.argv[1:]
if len(param) < 4:
    print("Erro: Insufficient parameters")
else:
    if FileChange(param[0],param[1],param[2],param[3]):
        print("Success - changes made")