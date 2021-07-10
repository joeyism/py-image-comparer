from pathlib import Path

from tqdm import tqdm
import requests

def download_model(model_path: Path, version="v1.0.0", block_Size=1024):
    model_url = f"https://github.com/joeyism/siamese-pytorch/releases/download/{version}/siamese-model.pt"
    response = requests.get(model_url, stream=True)
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    progress_bar = tqdm(desc="Downloading model", total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(model_path.as_posix(), 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")
