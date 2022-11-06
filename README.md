
# Datathon Entel 2022

Description:
The challenge is to develop a project that automates the review of clinical documents. Specifically in verifying the manual signature and extracting the date of the signature through an OCR module


### Entrenamiento

Se etiquetaron las imágenes de entrenamiento utilizando la herramienta labelimg obtenida de github. Más detalle se puede observar en la carpeta /training_data.

Se eligieron los pesos de las épocas con mejor performance. 

Los modelos implementados fueron:

* YOLOv3-SDF -> Es un modelo derivado de YOLOv3 cuya funcion es detectar fechas y firmas a partir del input de una imagen.

* YOLOv3-DOCR -> Es un modelo derivado de YOLOv3 cuya funcion es detectar y clasificar los números dentro de las fechas recortadas detectadas por el modelo YOLOv3-SDF.


### Dependencias

- Librería time
- Librería  os
- Librería opencv (4.5.2)
- Librería numpy 
- Librería pandas 

