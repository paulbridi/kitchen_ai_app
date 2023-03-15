from roboflow import Roboflow
from PIL import Image
import os
import numpy as np

def get_overlap(image1, image2):
    x1 = max(image1['left'], image2['left'])
    y1 = max(image1['top'], image2['top'])
    x2 = min(image1['right'], image2['right'])
    y2 = min(image1['bottom'], image2['bottom'])
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = (image1['right'] - image1['left']) * (image1['bottom'] - image1['top'])
    area2 = (image2['right'] - image2['left']) * (image2['bottom']- image2['top'])
    union = area1 + area2 - intersection
    overlap = intersection / union
    return overlap

def crop_fridge():

    rf = Roboflow(api_key=os.environ['ROBOFLOW_API'])
    project = rf.workspace().project("aicook-lcv4d")
    model = project.version(3).model

    try:
        output_json = model.predict(os.path.join("fridge_results","results.jpg"), confidence=50, overlap=0).json()
    except:
        return 'BAD PHOTO TRY AGAIN'
    im = Image.open(os.path.join("fridge_results","results.jpg"))

    image_list = []

    for item in output_json['predictions']:
        x = item['x']
        y = item['y']
        width = item['width']
        height = item['height']
        confidence = item['confidence']
        class_name = item['class']
        image = im.crop((x - (width/2), y - (height/2), x + (width/2), y + (height/2)))
        image_list.append({
            'image': image,
            'x': x,
            'y': y,
            'left': (x - (width/2)),
            'top': (y - (height/2)),
            'right': (x + (width/2)),
            'bottom': (y + (height/2)),
            'width': width,
            'height': height,
            'class': class_name,
            'confidence': confidence
        })

        image_list.sort(key=lambda x: x['confidence'], reverse=True)

        overlap_threshold = 0
        for i in range(len(image_list)):
            for j in range(i+1, len(image_list)):
                if image_list[i]['confidence'] == 0 or image_list[j]['confidence'] == 0:
                    continue
                overlap = get_overlap(image_list[i], image_list[j])
                if overlap > overlap_threshold:
                    image_list[j]['confidence'] = 0

        # create a new list with the non-overlapping detected images
        non_overlapping_images = []
        for image in image_list:
            if image['confidence'] > 0:
                non_overlapping_images.append((image['image'],image['class']))


    return (output_json, non_overlapping_images)
