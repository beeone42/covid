from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import qrcode
from datetime import datetime

now = datetime.now()

profil = {
    'PRENOM':  "Jean",
    'NOM':     "Dupont",
    'ADDR':    "1 rue de la paix",
    'CP':      "75001",
    'VILLE':   "Paris",
    'NE_LE':   "04/02/1942",
    'NE_A':    "La Bourboule",
    'RAISONS': ["courses"]
    }

def fill_item(profil, item, val):
    if item not in profil:
        profil[item] = val

    
def fill_profil(profil):
    
    fill_item(profil, 'FAIT_A',  profil['VILLE'])
    fill_item(profil, 'FAIT_LE', now.strftime("%d/%m/%Y"))
    fill_item(profil, 'FAIT_H',  now.strftime("%H"))
    fill_item(profil, 'FAIT_M',  now.strftime("%M"))

    fill_item(profil, 'SORT_LE', profil['FAIT_LE'])
    fill_item(profil, 'SORT_H',  profil['FAIT_H'])
    fill_item(profil, 'SORT_M',  profil['FAIT_M'])


###############################


def make_qrcode(profil, png):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=1
    )

    data = [
        "Cree le: %s a %sh%s" % (profil['FAIT_LE'], profil['FAIT_H'], profil['FAIT_M']),
        "Nom: %s" % profil['NOM'],
        "Prenom: %s" % profil['PRENOM'],
        "Naissance: %s a %s" % (profil['NE_LE'], profil['NE_A']),
        "Adresse: %s %s %s" % (profil['ADDR'], profil['CP'], profil['VILLE']),
        "Sortie: %s a %sh%s" % (profil['SORT_LE'], profil['SORT_H'], profil['SORT_M']),
        "Motifs: %s" % "-".join(profil['RAISONS']),
    ]

    qr.make(fit=True)
    ds = "; ".join(data)
    print(ds)
    qr.add_data(ds)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(png)


    
def make_attestation(profil, fname):

    fill_profil(profil)
    
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

    png = io.BytesIO()
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    page_width, page_height = can._pagesize

    can.setFont("Helvetica", 11)

    can.drawString(123, 686, "%s %s" % (profil['PRENOM'], profil['NOM']))
    can.drawString(123, 661, profil['NE_LE'])
    can.drawString( 92, 638, profil['NE_A'])
    can.drawString(134, 613, "%s %s %s" % (profil['ADDR'], profil['CP'], profil['VILLE']))

    can.drawString(111, 226, profil['FAIT_A'])
    can.drawString( 92, 200, profil['FAIT_LE'])
    can.drawString(200, 201, profil['FAIT_H'])
    can.drawString(220, 201, profil['FAIT_M'])


    can.setFont("Helvetica", 19)

    for r in profil['RAISONS']:
        can.drawString(X[r][0], X[r][1], "x")

        can.setFont("Helvetica", 11)

    make_qrcode(profil, png)
        
    png.seek(0)
    can.drawImage(ImageReader(png), page_width - QR_S_X, QR_S_Y, width = QR_S_W, height = QR_S_H, mask=None) 

    can.setFont("Helvetica", 7)
    can.drawString(464, 150, 'Date de creation:')
    can.drawString(455, 144, "%s a %s:%s" % (profil['FAIT_LE'], profil['FAIT_H'], profil['FAIT_M']))


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

    # page 2
    
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    png.seek(0)
    can.drawImage(ImageReader(png), QR_B_X, page_height - QR_B_Y, width = QR_B_W, height = QR_B_H, mask=None) 
    can.showPage()
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    page = new_pdf.getPage(0)
    output.addPage(page)


    # finally, write "output" to a real file
    outputStream = open(fname, "wb")
    output.write(outputStream)
    outputStream.close()


if __name__ == "__main__":
    make_attestation(profil, "./out/destination")
