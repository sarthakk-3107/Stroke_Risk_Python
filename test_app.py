import pytest
import pandas as pd
import numpy as np
from model import StrokeRiskModel
from data_loader import DataLoader

# Sample mock data for testing
sample_data = pd.DataFrame({
    "age": [65, 45],
    "hypertension": [1, 0],
    "heart_disease": [1, 0],
    "avg_glucose_level": [228.69, 105.92],
    "bmi": [36.6, 29.5]
})
sample_labels = [1, 0]

# Pytest fixture to create a temporary CSV and return a DataLoader instance
@pytest.fixture
def dummy_loader(tmp_path):
    # Write sample data with label column to a temporary CSV file
    filepath = tmp_path / "temp.csv"
    df = sample_data.copy()
    df["At Risk (Binary)"] = sample_labels
    df.to_csv(filepath, index=False)
    return DataLoader(str(filepath))

# Test if data loading returns correct shapes and labels
def test_load_data_shape(dummy_loader):
    X, X_scaled, y = dummy_loader.load_data()
    assert X.shape[0] == 2  # Two rows
    assert X_scaled.shape == (2, X.shape[1])  # Scaled data shape matches original
    assert y.tolist() == sample_labels  # Target values match the sample

# Test model training and check if prediction returns valid types
def test_model_training_and_prediction(dummy_loader):
    X, X_scaled, y = dummy_loader.load_data()
    model = StrokeRiskModel()
    model.train(X_scaled, y)
    prob, risk = model.predict([X_scaled[0]])
    assert isinstance(prob, float)  # Probability should be float
    assert risk in [0, 1]           # Risk prediction should be binary

# Ensure input transformation preserves the correct shape
def test_scaling_consistency(dummy_loader):
    _, X_scaled, _ = dummy_loader.load_data()
    input_df = sample_data.iloc[[0]]  # Take a single row
    transformed = dummy_loader.transform_input(input_df)
    assert transformed.shape == (1, input_df.shape[1])  # Shape must match feature count

# Validate probability output range is between 0–100%
def test_prediction_output_range(dummy_loader):
    X, X_scaled, y = dummy_loader.load_data()
    model = StrokeRiskModel()
    model.train(X_scaled, y)
    prob, _ = model.predict([X_scaled[0]])
    assert 0.0 <= prob <= 100.0  # Probability must be a valid percentage

# Check model raises error on invalid input shape
def test_exception_on_invalid_input():
    model = StrokeRiskModel()
    with pytest.raises(IndexError):
        model.predict([])  # Invalid input format (empty list)
