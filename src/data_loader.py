import os
import requests
from PIL import Image
import pandas as pd
from io import BytesIO
import json

class ImageDatasetLoader:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        self.create_data_folder()
        
    def create_data_folder(self):
        """Crea la carpeta de datos si no existe"""
        os.makedirs(self.data_folder, exist_ok=True)
        
    def download_image(self, url, filename):
        """Descarga una imagen desde una URL"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img.save(os.path.join(self.data_folder, filename))
                return True
            return False
        except Exception as e:
            print(f"Error descargando {url}: {str(e)}")
            return False
            
    def create_sample_dataset(self):
        """Crea un conjunto de datos de ejemplo con imágenes y metadatos"""
        # Lista de imágenes de ejemplo con sus URLs y metadatos
        sample_images = [
            {
                'url': 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=600',
                'filename': 'mountain1.jpg',
                'category': 'landscape',
                'description': 'Mountain landscape with snow'
            },
            {
                'url': 'https://images.unsplash.com/photo-1542744095-6f26b6144636?w=600',
                'filename': 'beach1.jpg',
                'category': 'landscape',
                'description': 'Sunny beach with palm trees'
            },
            {
                'url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600',
                'filename': 'cat1.jpg',
                'category': 'animal',
                'description': 'Cute cat sleeping'
            },
            {
                'url': 'https://images.unsplash.com/photo-1518791841217-8f162f1e1131?w=600',
                'filename': 'dog1.jpg',
                'category': 'animal',
                'description': 'Golden retriever puppy'
            },
            {
                'url': 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=600',
                'filename': 'food1.jpg',
                'category': 'food',
                'description': 'Colorful pizza'
            },
            {
                'url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600',
                'filename': 'car1.jpg',
                'category': 'vehicle',
                'description': 'Red sports car'
            }
        ]
        
        # Descargar imágenes
        print("Descargando imágenes de ejemplo...")
        for img_info in sample_images:
            if self.download_image(img_info['url'], img_info['filename']):
                print(f"Descargada {img_info['filename']}")
            else:
                print(f"Error descargando {img_info['filename']}")
        
        # Crear DataFrame con metadatos
        df = pd.DataFrame(sample_images)
        
        # Guardar DataFrame como CSV y JSON
        df.to_csv(os.path.join(self.data_folder, 'image_metadata.csv'), index=False)
        df.to_json(os.path.join(self.data_folder, 'image_metadata.json'), orient='records')
        
        print("\n¡Base de datos creada exitosamente!")
        print(f"Imágenes descargadas: {len(sample_images)}")
        print(f"Metadatos guardados en: {os.path.join(self.data_folder, 'image_metadata.csv')}")
        print(f"Metadatos guardados en: {os.path.join(self.data_folder, 'image_metadata.json')}")
        
        return df

if __name__ == "__main__":
    loader = ImageDatasetLoader()
    df = loader.create_sample_dataset()
    print("\nVista previa de los metadatos:")
    print(df.head())
