# Hugging Face Agents: Image Analysis Project

Este proyecto demuestra el uso de Hugging Face Agents para tareas de análisis de imágenes, incluyendo exploración de conjuntos de datos, clasificación de imágenes y detección de objetos. El proyecto está organizado para facilitar la claridad y el uso, siguiendo las mejores prácticas de reproducibilidad y modularidad.

## Estructura del Proyecto

```
Proyecto_hf_agents/
│
├── README.md                # Documentación del proyecto
├── requirements.txt         # Dependencias necesarias
├── .gitignore              # Archivos a ignorar por git
├── .yalm                   # Configuración de YAML
│
├── create_dataset.py       # Script para crear datasets
├── data/                   # Conjunto de datos de ejemplo
│   ├── car1.jpg           # Ejemplo de imagen de coche
│   ├── cat1.jpg           # Ejemplo de imagen de gato
│   ├── dog1.jpg           # Ejemplo de imagen de perro
│   ├── food1.jpg          # Ejemplo de imagen de comida
│   ├── mountain1.jpg      # Ejemplo de imagen de montaña
│   ├── sketch-mountains-input.jpg # Ejemplo de dibujo
│   ├── image_metadata.csv # Metadatos de imágenes
│   └── image_metadata.json # Metadatos de imágenes (formato JSON)
│
├── notebooks/              # Notebooks de Jupyter
│   ├── analisis_imagenes.ipynb # Análisis de imágenes
│   └── huggingface_models/     # Modelos de Hugging Face
│
└── src/                   # Código fuente
    ├── __pycache__/       # Archivos de caché de Python
    ├── data_loader.py     # Carga de datos
    └── image_utils.py     # Utilidades para imágenes
```

## Cómo Usar

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar los notebooks en la carpeta `notebooks/` para ver ejemplos prácticos.
3. Las imágenes de ejemplo están disponibles en la carpeta `data/`.

## Características
- Análisis descriptivo de conjuntos de datos
- Clasificación de imágenes usando modelos de Hugging Face
- Detección de objetos con modelos de Hugging Face
- Utilidades para manejo y procesamiento de imágenes
- Carga eficiente de datos

## Requisitos
- Python 3.8+
- Dependencias listadas en requirements.txt
- Jupyter Notebook para ejecutar los notebooks

## Contribución
Para contribuir al proyecto:
1. Hacer un fork del repositorio
2. Crear una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.
