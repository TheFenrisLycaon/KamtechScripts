from pdf2image import convert_from_path
from os import makedirs, listdir
import docx
from docx.shared import Inches


def makeImages(path, name):
    pages = convert_from_path(path)
    makedirs(name, exist_ok=True)
    for i in range(len(pages)):
        pages[i].save('{}/{:03d}.jpg'.format(name, i+1), 'JPEG')


def makeDoc(name):
    doc = docx.Document()
    imgs = sorted(listdir(f'./{name}/'))
    for i in imgs:
        doc.add_picture(f'./{name}/{i}', width=Inches(8.0))
    doc.save(f'{name}.docx')


def pdf2doc(path):
    path = path.split('/')[-1].split('\\')[-1]
    name = './' + path.split('.')[-2]
    makeImages(path, name)
    makeDoc(name)

#  Takes the pdf path as parameter
pdf2doc('./AutoBiography.pdf') 