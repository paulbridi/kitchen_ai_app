![alt text](https://raw.githubusercontent.com/canndyy/your_kitchen_ai/master/logo_1.jpeg)

# RECIPE RACCOON

Recipe Raccoon is an Computer Vision and NLP AI product built with Python that identify images of food ingredients and suggest customised recipes. For the full codebase, please see [this repo](https://github.com/canndyy/your_kitchen_ai). For a view of the (limited) demo, see [here](https://bit.ly/3FHS2Gv).

The product is a deep learning model that consists of:

1) Object detection Model - transfer learning from [Roboflow aicook](https://universe.roboflow.com/karel-cornelis-q2qqg/aicook-lcv4d)

2) Image Recognition Model - developed using Convolutional Neural Network (CNN) and Vision Transformer (ViT) with Tensorflow Keras

3) Recipe Processing Model - developed using Natural Language Processing (NLP) with Gensim Doc2vec

Built by [Candy](https://github.com/canndyy), [Louis](https://github.com/JammyNinja), and [Paul](https://github.com/paulbridi) in the Le Wagon Data Science bootcamp in March 2023.

## Datasets 

### Image dataset
We manually went through and used some images in the following 3 datasets, with some images also obtained through image web scrapping from mainstream supermarket websites, Google Shopping and Google Image.

Our final image dataset contains 26 classes of food ingredients with at least 300 images in each class after data augmentation.

[Fruits-262](https://www.kaggle.com/datasets/aelchimminut/fruits262)

[Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

[Fruits and Vegetables Image Recognition Dataset](https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition) - As of 22 Mar 23 this dataset contains incorrect images, with test images also found inside validation and training set. Filtering is required before using.

### Recipe dataset
[Food.com - Recipes and Reviews](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)
