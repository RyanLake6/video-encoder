#!/usr/bin/env python

import os
import argparse
from utils import get_bitrate, get_file_size, reformat_video, print_report

# Process all video files in the folder_path
def process_videos(folder_path: str, delete: bool, encoding: str, bitrate_arg: str):
    report = []
    total_saved_bytes = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(('.mp4', '.mov', '.avi', '.mkv')):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"rfmt_{filename}")
            
            print(f"Processing {input_path}...")
            bitrate = get_bitrate(input_path) if bitrate_arg == None else bitrate_arg
            if bitrate:
                original_size = get_file_size(input_path)
                success = reformat_video(input_path, output_path, bitrate, encoding)
                if success:
                    new_size = get_file_size(output_path)
                    saved_bytes = original_size - new_size
                    total_saved_bytes += saved_bytes
                    print(f"Original size: {original_size} bytes, New size: {new_size} bytes, Saved: {saved_bytes} bytes")
                    if delete:
                        os.remove(input_path)
                        print(f"Reformatted {filename} and deleted the original.")
                        report.append(f"Reformatted {filename} and deleted the original.")
                    else:
                        print(f"Reformatted {filename} and kept the original.")
                        report.append(f"Reformatted {filename} and kept the original")
                else:
                    print(f"Failed to reformat {filename}.")
                    report.append(f"Failed to reformat {filename}.")
            else:
                print(f"Could not determine bitrate for {filename}.")
                report.append(f"Could not determine bitrate for {filename}.")

    print_report(report, total_saved_bytes, folder_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reformat a collection of videos while preserving original bitrate")
    parser.add_argument("-d", "--delete", action='store_true', help="Delete the original files after reformat")
    parser.add_argument("-f", "--folder", type=str, required=True, help="Absolute folder path to the videos")
    parser.add_argument("-e", "--encoding", type=str, default="libx264", help="Encoding to use on videos (default is H.264)")
    parser.add_argument("-b", "--bitrate", type=str, help="Manually set the bitrate to encode to (default is to preserve original bitrate)")

    args = parser.parse_args()
    process_videos(args.folder, args.delete, args.encoding, args.bitrate)
