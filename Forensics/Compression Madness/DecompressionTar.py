import tarfile
import os

def decompress_nested_tars(start_tar, output_folder):
    current_tar = start_tar

    while current_tar.endswith(".tar"):
        try:
            with tarfile.open(current_tar, 'r') as tar_ref:
                tar_ref.extractall(output_folder)
            os.remove(current_tar)
            
            next_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith(".tar")]
            if not next_files:
                break
            current_tar = next_files[0]
        except tarfile.TarError:
            print(f"Bad TAR file: {current_tar}")
            break

starting_tar = "extracted/200.tar" 
output_dir = "extracted"
os.makedirs(output_dir, exist_ok=True)
decompress_nested_tars(starting_tar, output_dir)
