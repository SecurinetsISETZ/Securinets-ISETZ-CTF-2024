import zipfile
import os

def decompress_nested_zips(start_zip, output_folder):
    current_zip = start_zip
    
    while current_zip.endswith(".zip"):
        try:
            with zipfile.ZipFile(current_zip, 'r') as zip_ref:
                zip_ref.extractall(output_folder)
            os.remove(current_zip)
            
            next_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith(".zip")]
            if not next_files:
                break
            current_zip = next_files[0]
        except zipfile.BadZipFile:
            print(f"Bad ZIP file: {current_zip}")
            break

starting_zip = "200.zip"
output_dir = "extracted"
os.makedirs(output_dir, exist_ok=True)
decompress_nested_zips(starting_zip, output_dir)
