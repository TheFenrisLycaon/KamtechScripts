import shutil
import zipfile
import os
import fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


src_file = "temp/mai7.docx"  # input doc file path
out_dir = "temporary/run1/"  # temporary cache directory
des_file = "temp/mai7out.docx"  # output file path

with zipfile.ZipFile(src_file, 'r') as zip_ref:
    zip_ref.extractall(out_dir)

imgrep_path = "temporary/image_to_replace/image1.png"  # path of image to replace

media_path = os.path.join(out_dir, "word", "media")
img_file = os.path.join(media_path, "image1.jpeg")

os.remove(img_file)
shutil.copy(imgrep_path, img_file)


def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])


zip_directory(out_dir, des_file)
