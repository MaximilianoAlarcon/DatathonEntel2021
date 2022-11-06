
# Datathon Entel 2022

### Description
The challenge is to develop a project that automates the review of clinical documents. Specifically in verifying the manual signature and extracting the date of the signature through an OCR module


### Training
The training images were tagged using the labelimg tool obtained from github. More detail can be seen in the /training_data folder.

The weights of the times with the best performance were chosen.

The implemented models were:

YOLOv3-SDF -> It is a model derived from YOLOv3 whose function is to detect dates and signatures from the input of an image.

YOLOv3-DOCR -> It is a model derived from YOLOv3 whose function is to detect and classify the numbers within the trimmed dates detected by the YOLOv3-SDF model.


### Dependencies
- opencv library (4.5.2)
- numpy library
- panda bookstore
