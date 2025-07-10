import zipfile
import tarfile
import gzip
import bz2
import lzma
import py7zr
import shutil
import os

def detect_compression_type(filepath):
    with open(filepath, 'rb') as f:
        file_start = f.read(264)

    if file_start.startswith(b'\x50\x4B\x03\x04'):
        return 'zip'
    if file_start.startswith(b'\x1F\x8B'):
        return 'gz'
    if file_start.startswith(b'\x42\x5A\x68'):
        return 'bz2'
    if file_start.startswith(b'\xFD\x37\x7A\x58\x5A\x00'):
        return 'xz'
    if file_start.startswith(b'\x37\x7A\xBC\xAF\x27\x1C'):
        return '7z'
    if len(file_start) >= 264 and file_start[257:262] == b'ustar':
        return 'tar'
    return None

def extract_zip(filepath, output_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(output_dir)

def extract_tar(filepath, output_dir, mode='r:*'):
    with tarfile.open(filepath, mode) as archive:
        archive.extractall(output_dir)

def extract_gz(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with gzip.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_bz2(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with bz2.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_xz(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with lzma.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_7z(filepath, output_dir):
    with py7zr.SevenZipFile(filepath, mode='r') as archive:
        archive.extractall(path=output_dir)

def extract_file(filepath, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filetype = detect_compression_type(filepath)

    if filetype == 'zip':
        extract_zip(filepath, output_dir)
    elif filetype == 'tar':
        extract_tar(filepath, output_dir, 'r:')
    elif filetype == 'tar.gz':
        extract_tar(filepath, output_dir, 'r:gz')
    elif filetype == 'tar.bz2':
        extract_tar(filepath, output_dir, 'r:bz2')
    elif filetype == 'tar.xz':
        extract_tar(filepath, output_dir, 'r:xz')
    elif filetype == 'gz':
        extract_gz(filepath, output_dir)
    elif filetype == 'bz2':
        extract_bz2(filepath, output_dir)
    elif filetype == 'xz':
        extract_xz(filepath, output_dir)
    elif filetype == '7z':
        extract_7z(filepath, output_dir)
    else:
        raise ValueError(f"Filetype unsupported or not compressed: {filepath}")

def find_next_compressed_file(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            if detect_compression_type(full_path):
                return full_path
    return None

def get_file_in_path(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            return full_path
    return None

def decompress_until_plain_text(initial_path, work_dir):
    current_path = os.path.abspath(initial_path)
    iteration = 0

    while True:
        filetype = detect_compression_type(current_path)

        if not filetype:
            # print(f"Final extracted file without compression: {current_path}")
            break

        extract_dir = os.path.join(work_dir, f"step_{iteration}")
        extract_file(current_path, extract_dir)

        next_file = find_next_compressed_file(extract_dir)
        if not next_file:
            # print(f"Final extracted file without compression: {extract_dir}")
            # break
            return get_file_in_path(extract_dir)

        current_path = next_file
        iteration += 1