from pdf2image import convert_from_path as convert
import sys
from os import path, listdir, makedirs
import subprocess
from PIL import Image
from tqdm import tqdm

def compress(inFile, outPath, compressionLevel=3):
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    if not path.isfile(inFile):
        print("Error::\tInvalid path for input PDF file")
        sys.exit(1)

    if inFile.split('.')[-1].lower() != 'pdf':
        print("Error::\tInput file is not a PDF")
        sys.exit(1)

    initial_size = path.getsize(inFile)

    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[compressionLevel]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(outPath),
                     inFile]
                    )

    final_size = path.getsize(outPath)
    ratio = 1 - (final_size / initial_size)

    # print("Compression by {0:.0%}.".format(ratio))
    # print("Final file size is {0:.1f}MB".format(final_size / 1000000))

def toImg(filePath):
    name = filePath.split('/')[-1].split('.')[0]
    makedirs('./imgs/'+name, exist_ok=True)
    # print("Converting ...")
    pages = convert(filePath)
    count = 0
    # print("Saving...")
    for page in pages:
        page.save('./imgs/{}/{:03d}.jpg'.format(name, count+1), 'JPEG')
        count += 1

def compImg(folder):
    for img in sorted(listdir(f'./imgs/{folder}/')):
        makedirs(f'./compressed/{folder}', exist_ok=True)
        Image.open(f'./imgs/{folder}/' + img).save(f'./compressed/{folder}/'+img, format="JPEG", quality=25)



# for i in tqdm(sorted(listdir('./Data')), leave=False) : compress('./Data/'+ i, './out/'+i)
# for i in tqdm(sorted(listdir('./out')), leave= False): toImg('./out/'+ i)
for i in tqdm(sorted(listdir('./imgs')), leave=False): compImg(i) 
