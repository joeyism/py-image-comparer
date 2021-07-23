from typing import Union
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from torchvision import transforms

from .model import Siamese
from .download import download_model

ImageType = Union[Image.Image, np.ndarray]
DEFAULT_IMAGE_SIZE = (105, 105)
MODEL_FOLDER = Path(__file__).parents[1] / "models"
MODEL_FOLDER.mkdir(parents=True, exist_ok=True)
MODEL_PATH = MODEL_FOLDER / "siamese-model.pt"
if not MODEL_PATH.exists():
    download_model(MODEL_PATH)

model = Siamese()
model_dict = torch.load(MODEL_PATH, map_location="cpu")
model.load_state_dict(model_dict)

transformer = transforms.Compose(
    [
        transforms.Grayscale(),
        transforms.ToTensor(),
    ]
)

def _pil_image_(image: ImageType) -> Image:
    return Image.fromarray(np.array(image)).resize(DEFAULT_IMAGE_SIZE)


def is_similar(image1: ImageType, image2: ImageType, threshold=0.5) -> bool:
    return calculate_score(image1, image2) > threshold


def calculate_score(image1: ImageType, image2: ImageType) -> float:
    pil_image1 = _pil_image_(image1)
    pil_image2 = _pil_image_(image2)

    image_tensor1 = transformer(pil_image1).unsqueeze(0)
    image_tensor2 = transformer(pil_image2).unsqueeze(0)

    results = model(image_tensor1, image_tensor2)
    return results.detach().cpu().numpy()[0][0]
