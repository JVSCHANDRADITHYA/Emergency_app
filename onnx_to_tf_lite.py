import tensorflow as tf

# Load TensorFlow SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("tf_model")

# Convert the model
tflite_model = converter.convert()

# Save the TFLite model
with open("isolation_forest.tflite", "wb") as f:
    f.write(tflite_model)

print("Model converted to TensorFlow Lite successfully!")
