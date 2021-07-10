# py-image-comparer

## Installation
To install, run

```bash
pip install image-comparer
```

## Usage
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
