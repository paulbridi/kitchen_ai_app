from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras import models, layers, regularizers
from tensorflow.keras import metrics as mets
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow import cast, expand_dims, float32
import numpy as np
from tensorflow.image import resize


import matplotlib.pyplot as plt
import pickle #for history

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

batch_size = 16 #None = 1 #16 #32
IMG_SIZE = 224
seed_train_validation = 69 # Must be same for train_ds and val_ds

#path_to_dataset = os.path.join("..","..","data","food")
path_to_dataset = os.path.join("..","test_data","0_local_500")

path_to_dataset_train = os.path.join(path_to_dataset, "train")
path_to_dataset_test = os.path.join(path_to_dataset,  "test")
path_to_dataset_val = os.path.join(path_to_dataset,   "val")

#returns X_train, X_val, X_test
def load_data():
    """returns X_train, X_val, X_test
    """
    label_mode="int"
    X_train = image_dataset_from_directory(
        path_to_dataset_train,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=True
        )

    X_val = image_dataset_from_directory(
        path_to_dataset_val,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=True
        )

    X_test = image_dataset_from_directory(
        path_to_dataset_test,
        label_mode=label_mode,
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=False
        )
    return X_train,X_val,X_test

def show_one_image():
    count = 0
    test_image, test_label = None, None

    for image, label in X_train:#.take(1):
        if count == 0 :
            test_image = image.numpy()
            test_label = label.numpy()
        count+=1
        if count > 0: break

    #if you want to see an image
    print("test label:", test_label)
    print("first test label:", test_label[0])

    plt.imshow(test_image[0]/255)
    plt.title(target_dict[test_label[0]])

    return

#functions that we'll actually need...

def create_target_dict():
    classes_dict = {}
    classes_list = [
        'apple', 'avocado', 'banana',
        'beef', 'blueberry', 'broccoli',
        'cabbage', 'capsicum', 'carrot',
        'cauliflower', 'celery', 'chicken',
        'cucumber', 'eggplant', 'grape',
        'kiwi', 'lemon', 'lettuce', 'milk', 'mushroom',
        'onion','orange', 'pineapple',
        'pork', 'potato', 'strawberry',
        'tomato', 'white', 'zucchini' ]

    for i, food in enumerate(classes_list):
        classes_dict[i] = food

    return classes_dict

def load_best_model(model_name = "cnn_best_model", print_model = False):
    #load a model
    models_folder = os.path.join("","models")

    model_path = os.path.join(models_folder,model_name)

    model = models.load_model(model_path)

    print("loaded {model_name}:")

    if print_model:
        model.summary()
        print()

    return model

def make_predictions(img_list_in):
    print(f"making {len(img_list_in)} predictions...")

    predictions_out = []
    for img in img_list_in:
        #get one prediction
        food, confidence = make_one_prediction(img)
        #append to list
        predictions_out.append((food,confidence))

    print(predictions_out)

    return predictions_out

def make_one_prediction(img_in):

    prepped_img = convert_image(img_in)

    #load model already
    # model_name = "current_best_model"
    model = load_best_model()

    #add image to batch of one so can get prediction
    image = cast(expand_dims(prepped_img, 0), float32)


    result = model.predict(image)
    #result looks like [0.1, 0.4, 0.5]

    target_dict = create_target_dict()
    pred_encoded = result.argmax()
    #breakpoint()
    pred_class = target_dict[pred_encoded]
    confidence = result[0][pred_encoded] #batch size 1
    rounded_confidence = "{0:.1f}".format(confidence * 100)

    #plt.imshow the prediction!
    #plt.title(f"We are {rounded_confidence  }% sure that this is {pred_class}")
    #plt.imshow(img_in)

    return pred_class, rounded_confidence


if __name__ == "__main__":

    #X_train, X_val, X_test = load_data()
    target_dict = create_target_dict()

    X_test = image_dataset_from_directory(
        path_to_dataset_test,
        label_mode="int",
        color_mode="rgb",
        seed=seed_train_validation,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=batch_size,
        shuffle=False
        )

    count = 0
    test_image_batch, test_label_batch = None, None

    for image, label in X_test:
        if count == 0 :
            test_image_batch = image.numpy()
            test_label_batch = label.numpy()
        count+=1
        if count > 0: break

    test_image = test_image_batch[1]
    test_label = test_label_batch[1]
    #plt.imshow(test_image[0]/255)
    #plt.show()
    prediction, confidence = make_one_prediction(test_image)
    print("prediction: ", prediction)
    print("confidence: ", confidence)

    print("actual label: ", test_label)
    print("actual class: ", target_dict[test_label])

    #works but loads model everytime
    #make_predictions(test_image_batch)
    make_predictions_batch(test_image_batch)

#to save model from google cloud to home dir
#➜  your_kitchen_ai git:(la_package_start) ✗ gcloud compute scp jupyter@user-managed-notebook-1678200135:~/ ./location
#gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/current_best_model/ models/
#if asks for password then give it empty

 #gcloud compute scp --recurse jupyter@user-managed-notebook-1678200135:~/gh_folder/your_kitchen_ai/models/current_best_model/ models/cnn_best_model


def convert_image(img_in):
    IMG_SIZE=224
    rgb_image = img_in.convert('RGB')
    np_image = np.asarray(rgb_image)
    image_out = resize(np_image, [IMG_SIZE,IMG_SIZE])

    return image_out
