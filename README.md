# py-image-comparer
Compares two images using [Siamese Network](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) (Machine Learning) trained from a [Pytorch Implementation](https://github.com/joeyism/siamese-pytorch)

## Installation
To install, run

```bash
pip install image-comparer
```

## Usage

### CLI
```bash
image-compare
```
which wil show the follow help screen
```
usage: image-compare [-h] [--threshold THRESHOLD] Image1-Path Image2-Path
```

For example, you can compare two images with
```bash
image-compare tests/images/kobe.jpg tests/images/kobe2.jpg 
```
which gives the result
```
kobe.jpg and kobe2.jpg are not similar
```

### Programmatically
With PIL

```python
import image_comparer
from PIL import Image

image = Image.open("test/kobe.jpg")
image2 = Image.open("test/kobe2.jpg")
image_comparer.is_similar(image, image2, threshold=0.5)
```
or with OpenCV

```python
import image_comparer
import cv2

image = cv2.imread("test/kobe.jpg")
image2 = cv2.imread("test/kobe2.jpg")
image_comparer.is_similar(image, image2, threshold=0.5)
```

## API

### Methods

`is_similar(image1: Union[Image.Image, np.ndarray], image2: Union[Image.Image, np.ndarray], threshold=0.5)`: Checks if the two images are similar based on the reshold passed


`calculate_score(image1: Union[Image.Image, np.ndarray], image2: Union[Image.Image, np.ndarray])`: Calculates the score between the two images. The higher the score, the more closely the two images are related.


## Development

### Installation
```bash
pip install -r requirements-test.txt
```

### Tests
To run tests, run
```bash
pytest
```
