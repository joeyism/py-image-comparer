import torch
from model import Siamese
from PIL import Image
from torchvision import transforms

model = Siamese()
model_dict = torch.load("siamese-model.pt", map_location="cpu")
model.load_state_dict(model_dict)

transformer = transforms.Compose(
    [
        transforms.Grayscale(),
        transforms.ToTensor(),
    ]
)

if __name__ == "__main__":
    image = Image.open("test/kobe.jpg").resize((105, 105))
    image2 = Image.open("test/kobe2.jpg").resize((105, 105))

    image_tensor = transformer(image).unsqueeze(0)
    image2_tensor = transformer(image2).unsqueeze(0)
    model(image_tensor, image2_tensor)
