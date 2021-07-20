import shutil
import zipfile
import os
import fnmatch

os.makedirs('./.cache/', mode=0o777, exist_ok=True)
os.makedirs('./data/', mode=0o777, exist_ok=True)

def zipDir(folderPath, zipPath):
    with zipfile.ZipFile(zipPath, mode='w') as zipf:
        lenPath = len(folderPath)
        for root, _, files in os.walk(folderPath):
            for file in files:
                filePath = os.path.join(root, file)
                zipf.write(filePath, filePath[lenPath:])


def find(pattern, path):
    result = []
    for root, _, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def replaceImg(docPath, repImgNum, newImagePath):
    srcFile = docPath
    name = srcFile.replace('\\', '/').split('/')[-1].split('.')[0]
    cacheDir = f".cache/{name}/run1/"  # temporary cache directory
    destFile = f"data/{name}_changed.docx"  # output file path

    with zipfile.ZipFile(srcFile, 'r') as zip_ref:
        zip_ref.extractall(cacheDir)

    imgPath_rep = newImagePath  # path of image to replace
    imgName = newImagePath.replace('\\', '/').split('/')[-1]
    mediaPath = os.path.join(cacheDir, "word", "media")
    imgFile = os.path.join(mediaPath, f"image{repImgNum}.jpeg")

    os.remove(imgFile)
    shutil.copy(imgPath_rep, mediaPath)
    os.rename(os.path.join(mediaPath, imgName), os.path.join(mediaPath, f'image{repImgNum}.jpeg'))

    zipDir(cacheDir, destFile)

    # srcFile = str(input('Enter path to doc::\t')) # input doc file path


replaceImg('./src/docII.docx', 1, './static/wp4504903.jpg')
