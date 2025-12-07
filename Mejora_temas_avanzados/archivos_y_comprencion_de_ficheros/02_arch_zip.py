
import zipfile
from zipfile import ZipFile

with zipfile.ZipFile('archivo.zip','w') as fzip:
    fzip.write("doc.txt")
    fzip.printdir()


