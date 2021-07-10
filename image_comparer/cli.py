from pathlib import Path
import argparse

import cv2

from .compare import is_similar


def cli():
    parser = argparse.ArgumentParser(description='Compares two images')
    parser.add_argument('image1', metavar="Image1-Path", type=Path, help='first image in comparison')
    parser.add_argument('image2', metavar="Image2-Path", type=Path, help='second image in comparison')
    parser.add_argument('--threshold', type=float, default=0.5, help='threshold limit (default: 0.5)')
    args = parser.parse_args()
    main(args.image1, args.image2)

def main(image1_path: Path, image2_path: Path):
    image1 = cv2.imread(image1_path.as_posix())
    image2 = cv2.imread(image2_path.as_posix())
    if is_similar(image1, image2):
        print(f"{image1_path.name} and {image2_path.name} are similar")
    else:
        print(f"{image1_path.name} and {image2_path.name} are not similar")

if __name__ == "__main__":
    cli()
