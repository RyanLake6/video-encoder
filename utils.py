import math
import os
import subprocess

# Fetch the bitrate of the specified original file
def get_bitrate(file_path):
    result = subprocess.run(
        ['ffmpeg', '-i', file_path],
        stderr=subprocess.PIPE,
        universal_newlines=True
    )
    output = result.stderr
    bitrate_line = [line for line in output.split('\n') if 'bitrate:' in line]
    if bitrate_line:
        bitrate = bitrate_line[0].split('bitrate:')[1].strip().split(' ')[0] + 'k'
        return bitrate
    return None

# Reformat video utilizing ffmpeg
def reformat_video(file_path: str, output_path: str, bitrate: str, encoding: str):
    result = subprocess.run(
        ['ffmpeg', '-i', file_path, '-c:v', encoding, '-b:v', bitrate, '-c:a', 'copy', output_path]
    )
    return result.returncode == 0

# Fetches the file size of the file path
def get_file_size(file_path: str):
    return os.path.getsize(file_path)

# Print full report of debug info
def print_report(report, saved_bytes, folder_path):
    print('\n\n************************')
    print(f"REPORT for all video encodings at: {folder_path} \n")

    for string in report:
        print(string, end='\n')

    size_saved = readable_size(saved_bytes)

    print('\n')
    print(f'Total storage reclaimed if originals are deleted is: {size_saved}')
    print('************************')

# convert the number of bytes into the best unit for readability
def readable_size(size_in_bytes):
    if size_in_bytes == 0:
        return "0B"
    
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_in_bytes / p, 2)
    return f"{s} {size_name[i]}"