from pdf2image import convert_from_path
from os import makedirs, listdir
import sys
from tqdm import tqdm
import docx
from docx.shared import Inches, Cm


def makeImages(path, name):
    pages = convert_from_path(path)
    makedirs(name, exist_ok=True)
    print("\nConverting ...\n")
    for i in tqdm(range(len(pages))):
        pages[i].save('{}/{:03d}.jpg'.format(name, i+1), 'JPEG')
    print("\nImages Saved !\n")


def makeDoc(name):
    doc = docx.Document()
    sections = doc.sections

    for section in sections:
        # TODO : Set margins
        section.top_margin =    Cm(0)
        section.bottom_margin = Cm(0)
        section.left_margin =   Cm(0)
        section.right_margin =  Cm(0)
    
    imgs = sorted(listdir(f'./{name}/'))
    
    print("\nCreating Doc file...\n")
    for i in tqdm(imgs):
        doc.add_picture(f'./{name}/{i}', width=Inches(8.0))
    
    doc.save(f'{name}.docx')
    print("\nDoc Saved...\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You can also run the script py passing the path to pdf.\nFor example::python3 main.py path/to/pdf.pdf")
        path = input("Enter file path ::\t")
    else:
        path = sys.argv[1]
    
    path = path.split('/')[-1]
    path = path.split('\\')[-1]

    name = './' + path.split('.')[-2]
    makeImages(path, name)
    makeDoc(name)
    print("\nDone !\n")
