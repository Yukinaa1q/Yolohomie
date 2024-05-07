from keras.models import load_model
import cv2
import numpy as np
from collections import Counter

def get_image_prediction(image, model, class_names):
    # Resize the image
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape
    image_array = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image_normalized = (image_array / 127.5) - 1

    # Predict using the model
    prediction = model.predict(image_normalized)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score * 100

# Capture images from the camera for 3 seconds
def capture_images(camera_index):
    camera = cv2.VideoCapture(camera_index)
    images = []
    start_time = cv2.getTickCount()

    while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < 3:
        ret, frame = camera.read()
        if not ret:
            break
        images.append(frame)

    camera.release()
    return images

# Example usage:

def get_prediction():
    camera_index = 0  # Change this index to match your camera (0 or 1 usually)
    model_path = "keras_Model.h5"
    labels_path = "labels.txt"
    
    # Load the model and labels
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()

    # Capture images from the camera for 3 seconds
    images = capture_images(camera_index)

    # Perform predictions on each captured image
    predictions = []
    for image in images:
        class_name, confidence_score = get_image_prediction(image, model, class_names)
        predictions.append(class_name)

    # Determine the most frequent prediction
    most_common_prediction = Counter(predictions).most_common(1)[0][0]
    # print("Most frequent prediction:", most_common_prediction)
    return most_common_prediction

if __name__ == "__main__":
    print(get_prediction())