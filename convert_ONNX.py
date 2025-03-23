import skl2onnx
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Load trained Isolation Forest model and scaler
model = joblib.load("isolation_forest_model.pkl")
scaler = joblib.load("scaler.pkl")

# Define input type (3 features: a_x, a_y, a_z)
input_type = [("input", FloatTensorType([None, 3]))]

# Convert to ONNX with explicit opset version
onnx_model = convert_sklearn(model, initial_types=input_type, target_opset=12)  # Change 12 if necessary

# Save ONNX model
with open("isolation_forest.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())

print("Model converted to ONNX successfully!")
