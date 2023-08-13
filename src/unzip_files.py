import zipfile
import os

target_extensions = ['zip', 'rar']

def filter_compacted():
    compacted_files = []
    for file in os.listdir('data-raw'):
        ext = file.split('.')[-1]
        if ext in target_extensions:
            compacted_files.append(file)
    return(compacted_files)

def extract_files(): ## need to fix to consider rar files
    for file in filter_compacted():
        with zipfile.ZipFile('data-raw/' + file, 'r') as zip_ref:
            zip_ref.extractall('data-raw')

