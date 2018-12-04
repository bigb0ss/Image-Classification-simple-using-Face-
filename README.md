# Face-Detection-Simple
Detects your mouth is opened or not from a live camera feed


It uses an image dataset of 2160 images ,

1050 of Open mouth images and remaining of Closed Mouth Images

The dataset is created using the Open CV toolkit of python

A Convolutional Model is trained on the gray scale images of the dataset with an accuracy off 97%

Pythons Pickle package is used to create an api of the model, which is used to deploy

The trained model is deployed along with the OpenCV , which runs live camera feed from the web camera

The application classifies the image , at every frame of the live video feed from the web camera
