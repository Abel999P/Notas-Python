
import gzip


with open("python.docx","rb") as file:
    with gzip.open("fichero.txt.gz","wb") as fichero:
        fichero.writable(file)

