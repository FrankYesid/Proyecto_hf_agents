import os
from typing import List, Tuple
from PIL import Image
import pandas as pd
import torch
from transformers import pipeline


def load_images_from_folder(folder: str) -> List[Image.Image]:
    """Load all images from a folder and return as a list of PIL Images."""
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder, filename)
            images.append(Image.open(img_path))
    return images


def dataset_descriptive_stats(folder: str) -> pd.DataFrame:
    """Return a DataFrame with basic info (filename, size, mode) for all images in a folder."""
    data = []
    for filename in os.listdir(folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder, filename)
            with Image.open(img_path) as img:
                data.append({
                    "filename": filename,
                    "size": img.size,
                    "mode": img.mode
                })
    return pd.DataFrame(data)


def classify_image(image: Image.Image, model_name: str = "google/vit-base-patch16-224") -> dict:
    """Classify an image using a Hugging Face image classification pipeline."""
    classifier = pipeline("image-classification", model=model_name)
    return classifier(image)


def detect_objects(image: Image.Image, model_name: str = "facebook/detr-resnet-50") -> dict:
    """Detect objects in an image using a Hugging Face object detection pipeline."""
    detector = pipeline("object-detection", model=model_name)
    return detector(image) 