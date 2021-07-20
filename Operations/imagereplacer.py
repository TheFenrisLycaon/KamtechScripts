import shutil
import zipfile
import os
import fnmatch


def zipDir(folderPath, zipPath):
    with zipfile.ZipFile(zipPath, mode='w') as zipf:
        lenPath = len(folderPath)
        for root, _, files in os.walk(folderPath):
            for file in files:
                filePath = os.path.join(root, file)
                zipf.write(filePath, filePath[lenPath:])


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


os.makedirs('./.cache/', mode=0o777, exist_ok=True)
os.makedirs('./data/', mode=0o777, exist_ok=True)

srcFile = "src/doc.docx"  # input doc file path
# srcFile = str(input('Enter path to doc::\t')) # input doc file path
name = srcFile.replace('\\', '/').split('/')[-1].split('.')[0]
destDir = f".cache/{name}/run1/"  # temporary cache directory
destFile = f"data/{name}_changed.docx"  # output file path

with zipfile.ZipFile(srcFile, 'r') as zip_ref:
    zip_ref.extractall(destDir)

imgPath_rep = "./static/image1.png"  # path of image to replace
mediaPath = os.path.join(destDir, "word", "media")
imgFile = os.path.join(mediaPath, "image1.jpeg")

os.remove(imgFile)
shutil.copy(imgPath_rep, imgFile)

zipDir(destDir, destFile)