import xml.etree.ElementTree as ET
import sys
import traceback

base = r"c:\Users\fna003\OneDrive - UiT Office 365\Faglig\Python\Book\Code\tb_sc_wise_qti\ch_08_basic_class_objects_qti"
paths = [base + "\\assessmentTest.xml"]
paths += [f"{base}\\items\\item{i}.xml" for i in range(1,7)]

ok = True
for p in paths:
    try:
        ET.parse(p)
        print(p + ': OK')
    except Exception:
        print(p + ': ERROR ->')
        traceback.print_exc()
        ok = False

if not ok:
    sys.exit(2)
