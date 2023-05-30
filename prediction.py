import matplotlib.pyplot as plt
import keras_ocr

# Load the pre-trained model
pipeline = keras_ocr.pipeline.Pipeline()

# Provide an image for OCR
image_path = '/Users/jeremie/Desktop/flask-api/01.jpeg'
image = keras_ocr.tools.read(image_path)

# Perform OCR
predictions = pipeline.recognize(image)

# Convert image and predictions to appropriate data types
image_array = keras_ocr.tools.image.img_to_array(image)
predictions_array = keras_ocr.detection.convert_annotations_to_arrays(predictions[0])

Display the results
fig, axs = plt.subplots(figsize=(10, 10))
axs.imshow(image_array.astype('uint8'))  # Convert image to float data type
axs = keras_ocr.detection.drawAnnotations(axs, predictions_array)  # Use drawAnnotations from detection module
plt.axis('off')
plt.show()
