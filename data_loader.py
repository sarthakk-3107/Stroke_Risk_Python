import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataLoader:
    def __init__(self, filepath):
        # Store the path to the CSV file
        self.filepath = filepath
        # Initialize a standard scaler for feature normalization
        self.scaler = StandardScaler()

    def load_data(self):
        # Read the dataset from the provided file path
        df = pd.read_csv(self.filepath)

        # Assume all columns except the last two are features
        X = df.iloc[:, :-2]

        # Target label for classification
        y = df["At Risk (Binary)"]

        # Scale the feature values to have mean=0 and std=1
        X_scaled = self.scaler.fit_transform(X)

        # Return the raw features, scaled features, and labels
        return X, X_scaled, y

    def transform_input(self, input_df):
        # Apply the same scaling to new input data using the fitted scaler
        return self.scaler.transform(input_df)
