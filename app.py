from bottle import abort, route, run, get, post, request, response, template, static_file
import subprocess, os, json, sys, io
from covid import make_attestation
import uuid

pdf      = io.BytesIO()
pdf_key  = "key..."
pdf_name = "name..."

CONFIG_FILE = 'config.json'

"""
Open and load a file at the json format
"""

def open_and_load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            try:
                return json.loads(config_file.read())
            except:
                print("can't decode", CONFIG_FILE)
                sys.exit(2)
    else:
        print("File [%s] doesn't exist, aborting." % (CONFIG_FILE))
        sys.exit(1)


def make_pdf_name(profil):
    d = profil['SORT_LE']
    h = profil['SORT_H']
    m = profil['SORT_M']
    j = "%s%s%s-%s%s-%s-%s" % (d[6:10], d[3:5], d[0:2], h, m, profil['PROFIL_NAME'], profil['RAISONS'][0])
    return (j)
    
@route('/')
def hello():
    return template('hello')

@get("/pdf/<filepath:re:.*\.pdf>")
def static_pdf(filepath):
    global pdf
    global pdf_key
    global pdf_name

    if (filepath != pdf_key):
        abort(404, 'not found')
    response.set_header('Content-type', 'application/pdf')
    response.set_header("Content-Disposition", "attachment; filename=%s" % pdf_name)
    response.content_length = len(pdf.getvalue())
    pdf.seek(0)
    return pdf.getvalue()

    
@route('/gen', method=['GET', 'POST'])
def gen():
    global pdf
    global pdf_key
    global pdf_name
    
    print("gen")

    del pdf
    pdf = io.BytesIO()

    profil = {}
    for (k, v) in request.params.allitems():
        if (k == 'raisons'):
            profil['RAISONS'] = [v]
        else:
            profil[k.upper()] = v

    if ('AUTO' in profil):
        if ('FAIT_LE' in profil):
            del profil['FAIT_LE']
        del profil['FAIT_H']
        del profil['FAIT_M']
        del profil['SORT_LE']
        del profil['SORT_H']
        del profil['SORT_M']
            
    pdf.seek(0)
    pdf.write(make_attestation(profil).read())
    print(type(pdf))
    pdf_name = "attestation-%s.pdf" % make_pdf_name(profil)
    pdf_key = "%s.pdf" % uuid.uuid4().hex

    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return pdf_key
    else:
        response.set_header('Content-type', 'application/pdf')
        response.set_header("Content-Disposition", "attachment; filename=%s" % pdf_name)
        response.content_length = len(pdf.getvalue())
        pdf.seek(0)
        return pdf.getvalue()

if __name__ == "__main__":
    config = open_and_load_config()
    run(host=config["host"], port=config["port"], debug=config["debug"])
