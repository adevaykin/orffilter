import sys
import os
from pathlib import Path

def is_debug():
    return False

def main():
    if len(sys.argv) != 2:
        print("Specify working directory as script execution argument, e.g.: python orffilter.py input", file=sys.stderr)
        exit()

    input_path = os.path.abspath(sys.argv[1])
    print(f"Input directory: {input_path}")
    orfs = find_orfs(input_path)
    jpgs = find_jpgs(input_path)

    if is_debug():
        for o in orfs:
            print(f"{o}: {orfs[o]}")
        for j in jpgs:
            print(f"{j}")

    deleted_files_count = 0
    for orf in orfs:
        if orf not in jpgs:
            for o in orfs[orf]:
                deleted_files_count += 1
                if is_debug():
                    print(f"Delete ORF {o}")
    
    print(f"Deleted {deleted_files_count} ORF files.")
    print("~~ Thank you for using our service! ~~")

def find_orfs(input_dir):
    print("Searching for ORF files...")
    orfs = dict()
    for o in Path(input_dir).rglob('*.orf'):
        filename = os.path.basename(o).split(".")[0]
        prev_entries = orfs.get(filename, list())
        orfs.update({ filename: prev_entries + list({o}) })
    print(f"    Found {len(orfs)}+ ORF files.")
    return orfs

def find_jpgs(input_dir):
    print("Searching for JPG/JPEG files...")
    jpgs = set()
    for j in Path(input_dir).rglob('*.jpg'):
        filename = os.path.basename(j).split(".")[0]
        jpgs.add(filename)
    for j in Path(input_dir).rglob('*.jpeg'):
        filename = os.path.basename(j).split(".")[0]
        jpgs.add(filename)
    print(f"    Found {len(jpgs)} JPG/JPEG files.")
    return jpgs

if __name__ == "__main__":
    main()
