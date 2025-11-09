import pandas as pd
import numpy as np
import qrcode
from PIL import Image
import configparser
from pathlib import Path
import os
import shutil

BASE_DIR = Path(__file__).parent
cpath = BASE_DIR / 'logos.conf'

# cpath =  r"\folders.conf"
config = configparser.ConfigParser()
config.read(cpath)

def get_logos():
    logo_list = config.get('logos', 'logo').split(", ")
    return logo_list

def get_save_folder():
    save_path = config.get('save', 'save_path')
    return save_path

def make_qr(data: str, file_name: str, save_folder: str, logo_path: str):
    
    os.makedirs(save_folder, exist_ok=True)  # Create folder if it doesn’t exist
    # File path for saving
    save_path = os.path.join(save_folder, file_name)
    
    # Generate QR code
    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 5, border = 4)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create and save QR image
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    # === ADD LOGO ===
    if logo_path != None:    
        if os.path.exists(logo_path):
            logo = Image.open(logo_path)
        
            # Compute logo size (about 15–20% of QR code size)
            width, height = img.size
            logo_size = int(width * 0.2)
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
            # Compute position (center)
            x = (width - logo_size) // 2
            y = (height - logo_size) // 2
        
            # Paste logo with transparency mask if available
            img.paste(logo, (x, y), mask=logo if logo.mode == "RGBA" else None)
        else:
            print("Logo file not found. Creating QR without logo.")
    
    img.save(save_path)

def clear_folder(folder_path):
    """Delete all contents of the folder if it exists"""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


file = input("Enter file path to process: ")
file = file.replace('"', '')
# Detect available sheets
try:
    sheet_names = pd.ExcelFile(file).sheet_names
    print("\nAvailable Sheets:")
    for idx, name in enumerate(sheet_names, start=1):
        print(f"{idx}. {name}")

    sheet_choice = int(input("\nSelect sheet number to process: "))
    sheet_name = sheet_names[sheet_choice - 1]

    print(f"\nUsing sheet: {sheet_name}")
except Exception as e:
    print("Error reading sheets:", e)
    exit()
data = pd.read_excel(file, sheet_name = sheet_name)

logos = get_logos()
print("Select logo to include in QR: ")
count = 1
logo_dict = {}
for i in logos:
    splits = i.split("\\")
    logo_name = splits[-1]
    print(f"{count}. {logo_name}")
    logo_dict[count] = logo_name
    count += 1
print(f"{count}. No logo")
logo = int(input("Enter choice of logo: "))
if logo != count:
    logo_path = logos[logo-1]
else:
    logo_path = None

choice = int(input(f"Enter name of column to use: {data.columns()}\nEnter choice: "))
strings = list(data[choice])
save_folder = get_save_folder()
clear_folder(save_folder)
# filenames = [i for i in range(1, len(strings) + 1)]
# seconds = len(filenames) // 8
# minutes = seconds // 60
# print("Estimated time for generation: ", minutes, "minutes")
for i in strings:
    make_qr(strings[i], i, save_folder, logo_path)
print("Done Processing.")