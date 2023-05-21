# Import necessary libraries
import argparse
import time
import numpy as np
import tensorflow as tf
import cv2
import time


def load_labels(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def preprocess_image(image, input_mean, input_std):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (width, height))
    image = (image.astype(np.float32) - input_mean) / input_std
    image = np.expand_dims(image, axis=0)
    return image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    # Load the TFLite model and allocate tensors
    interpreter = tf.lite.Interpreter(
        model_path='/tmp/model_unquant.tflite')
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Get input shape and model details
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    floating_model = input_details[0]['dtype'] == np.float32
    labels = load_labels('/tmp/labels.txt')

    # Initialize camera capture
    capture = cv2.VideoCapture(1)  # Use the default camera (change the index if needed)

    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()

        # Preprocess the frame
        input_data = preprocess_image(frame, 127.5, 127.5)

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()

        # Get the output tensor and post-process the results
        output_data = interpreter.get_tensor(output_details[0]['index'])
        results = np.squeeze(output_data)
        top_k = results.argsort()[-5:][::-1]

        # Display the results
        for i in top_k:
            if floating_model:
                label = labels[i]
            else:
                label = labels[i]
            print(label)
        print("\n")
        time.sleep(1.5)