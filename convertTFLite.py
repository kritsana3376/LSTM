import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("my_lstm_model.keras")

# Create a TFLite Converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Allow TF Lite to use some TensorFlow ops
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,    # Use built-in TFLite operations
    tf.lite.OpsSet.SELECT_TF_OPS       # Enable select TensorFlow operations
]

# Disable experimental lowering of tensor lists (fixes the TensorListReserve issue)
converter._experimental_lower_tensor_list_ops = False

# Convert the model
tflite_model = converter.convert()

# Save the model
with open("model.tflite", "wb") as f:
    f.write(tflite_model)

print("Model successfully converted to TFLite!")