#! /home/fenris/anaconda3/envs/webapp/bin/python
from pdf2image import convert_from_path as convert
import sys
from os import path, listdir, makedirs
import subprocess
from PIL import Image
from tqdm import tqdm

quality = {
    0: '/default',
    1: '/prepress',
    2: '/printer',
    3: '/ebook',
    4: '/screen'
}

makedirs('./PDFCompression', exist_ok=True)
makedirs('./ImageCompression', exist_ok=True)
makedirs('./ImageConversion', exist_ok=True)


def compress(inFile, outPath, compressionLevel=3):

    makedirs('./PDFCompression', exist_ok=True)

    if not path.isfile(inFile):
        print("Error::\tInvalid path for input PDF file")
        sys.exit(1)

    if inFile.split('.')[-1].lower() != 'pdf':
        print("Error::\tInput file is not a PDF")
        sys.exit(1)

    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[compressionLevel]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(outPath),
                     inFile]
                    )

    # Uncomment to see compression stats
    # initial_size = path.getsize(inFile)
    # final_size = path.getsize(PDFCompressionPath)
    # ratio = 1 - (final_size / initial_size)
    # print("Compression by {0:.0%}.".format(ratio))
    # print("Final file size is {0:.1f}MB".format(final_size / 1000000))


def toImg(filePath):
    name = filePath.split('/')[-1].split('.')[0]
    makedirs('./ImageConversion/'+name, exist_ok=True)
    pages = convert(filePath)
    count = 0
    for page in pages:
        page.save('./ImageConversion/{}/{:03d}.jpg'.format(name, count+1), 'JPEG')
        count += 1


def compImg(folder):
    for img in sorted(listdir(f'./ImageConversion/{folder}/')):
        makedirs(f'./ImageCompression/{folder}', exist_ok=True)
        Image.open(f'./ImageConversion/{folder}/' + img).save(
            f'./ImageCompression/{folder}/'+img, format="JPEG", quality=25)


for i in tqdm(sorted(listdir('./Source')), leave=False):
    compress('./Source/' + i, './PDFCompression/'+i)
for i in tqdm(sorted(listdir('./PDFCompression')), leave=False):
    toImg('./PDFCompression/' + i)
for i in tqdm(sorted(listdir('./ImageConversion')), leave=False):
    compImg(i)
