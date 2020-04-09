from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import qrcode
from datetime import datetime

now = datetime.now()

PRENOM   = "Jean"
NOM      = "Dupont"
ADDR     = "1 rue de la paix"
CP       = "75001"
VILLE    = "Paris"

NE_LE    = "04/02/1942"
NE_A     = "La Bourboule"

FAIT_A   = VILLE
FAIT_LE  = now.strftime("%m/%d/%Y")
FAIT_H   = now.strftime("%H")
FAIT_M   = now.strftime("%M")

SORT_LE  = FAIT_LE
SORT_H   = FAIT_H
SORT_M   = FAIT_M

RAISONS  = ["courses", "sport"]



###############################

QR_S_X   = 170
QR_S_Y   = 155
QR_S_W   = 100
QR_S_H   = 100

QR_B_X   = 50
QR_B_Y   = 350
QR_B_W   = 300
QR_B_H   = 300

X = {
    'travail'    : [76, 527],
    'courses'    : [76, 478],
    'sante'      : [76, 436],
    'famille'    : [76, 400],
    'sport'      : [76, 345],
    'judiciaire' : [76, 298],
    'missions'   : [76, 260]
}

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
page_width, page_height = can._pagesize

can.setFont("Helvetica", 11)

can.drawString(123, 686, "%s %s" % (PRENOM, NOM))
can.drawString(123, 661, NE_LE)
can.drawString( 92, 638, NE_A)
can.drawString(134, 613, "%s %s %s" % (ADDR, CP, VILLE))

can.drawString(111, 226, FAIT_A)
can.drawString( 92, 200, FAIT_LE)
can.drawString(200, 201, FAIT_H)
can.drawString(220, 201, FAIT_M)


can.setFont("Helvetica", 19)

for r in RAISONS:
    can.drawString(X[r][0], X[r][1], "x")

can.setFont("Helvetica", 11)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=1
)

data = [
    "Cree le: %s a %s:%s" % (FAIT_LE, FAIT_H, FAIT_M),
    "Nom: %s" % NOM,
    "Prenom: %s" % PRENOM,
    "Naissance: %s a %s" % (NE_LE, NE_A),
    "Adresse: %s %s %s" % (ADDR, CP, VILLE),
    "Sortie: %s a %sh%s" % (SORT_LE, SORT_H, SORT_M),
    "Motifs: %s" % "-".join(RAISONS),
]

qr.make(fit=True)
ds = "; ".join(data)
print(ds)
qr.add_data(ds)



img = qr.make_image(fill_color="black", back_color="white")
img.save('qr.png')

can.drawImage('qr.png', page_width - QR_S_X, QR_S_Y, width = QR_S_W, height = QR_S_H, mask=None) 

can.setFont("Helvetica", 7)
can.drawString(464, 150, 'Date de creation:')
can.drawString(455, 144, '08/04/2020 a 13h05')


can.showPage()
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("original.pdf", "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)



packet = io.BytesIO()
#packet.seek(0)
can = canvas.Canvas(packet, pagesize=A4)
can.drawImage('qr.png', QR_B_X, page_height - QR_B_Y, width = QR_B_W, height = QR_B_H, mask=None) 
can.showPage()
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
page = new_pdf.getPage(0)
output.addPage(page)


# finally, write "output" to a real file
outputStream = open("./out/destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
