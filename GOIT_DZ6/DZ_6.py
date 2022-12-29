import shutil
from pathlib import Path
import sys
unknown_ext = set()
known_ext = set()
x = sys.argv[1]
files_by_ext = {'images':[],'video':[],'documents':[],'music':[],'archives':[]}
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "'", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}
for i, j in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(i)] = j
    TRANS[ord(i.upper())] = j.upper()


def sort_trash(folder):
    global unknown_ext,known_ext
    target = Path(folder)
    for f in target.iterdir():
        ext = f.suffix
        pref = f.name.removesuffix(ext)
        transF = normalize(pref)
        newF = target.joinpath(folder,transF+ext)
        f.rename(newF)

    for f in target.iterdir():
        if f.is_dir():
            if f.name.casefold() in 'archives, video, audio, documents, images':
                continue
            elif not any(f.iterdir()):
                f.rmdir()
                continue
            else:
                sort_trash(f)
        else:
            dst = sort_files_by_extensions(f, target, folder)
            if dst == 'archives':
                continue
            elif len(dst) != 0:
                dst_dir = target.joinpath(folder, dst)
                dst_dir.mkdir(parents=True, exist_ok=True)
                files_by_ext[dst].append(f.name)
                shutil.move(f, dst_dir)
            else:
                continue
    return files_by_ext,known_ext,unknown_ext


def sort_files_by_extensions(file, target, folder):
    global known_ext, files_by_ext, unknown_ext
    ext = file.suffix
    ext = ext.upper()
    dst = ''
    if ext in ['.ZIP', '.GZ', '.TAR', '.RAR', '.7Z']:
        dst = 'archives'
        known_ext.add(ext)
        files_by_ext[dst].append(file.name)
        dot = file.name.index('.')
        subfolder = Path(file.name[:dot])
        dst_dir = target.joinpath(subfolder, dst)
        subfolder.mkdir(parents=True, exist_ok=True)
        dst_dir.mkdir(parents=True, exist_ok=True)
        shutil.unpack_archive(file, subfolder)
        shutil.move(subfolder, dst_dir)
        file.unlink(missing_ok=True)
    else:
        if ext in ['.JPEG', '.PNG', '.JPG', '.SVG']:
            dst = 'images'
        elif ext in ['.AVI', '.MP4', '.MOV', '.MKV']:
            dst = 'video'
        elif ext in ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLS', '.XLSX', '.PPTX']:
            dst = 'documents'
        elif ext in ['.MP3', '.OGG', '.WAV', '.AMR', '.M4A']:
            dst = 'music'
        else:
            unknown_ext.add(ext)
            pass
        known_ext.add(ext)
    return dst


def normalize(name):
    global TRANS
    translit = name.translate(TRANS)
    for letter in translit:
        if ord(letter) in range (65, 91) or ord(letter) in range (97, 123) or ord(letter) in range (48, 58):
            continue
        else:
            translit = translit.replace(letter,'_')
    return translit


sort_trash(x)