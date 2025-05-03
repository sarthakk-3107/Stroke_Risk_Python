from sklearn.ensemble import RandomForestClassifier

class StrokeRiskModel:
    def __init__(self):
        # Initialize a Random Forest classifier with 100 trees and a fixed random state for reproducibility
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, X_scaled, y):
        # Train the Random Forest model using the scaled features and corresponding labels
        self.model.fit(X_scaled, y)

    def predict(self, x_scaled):
        # Predict the probability of the positive class (stroke risk)
        prob = self.model.predict_proba(x_scaled)[0][1] * 100  # Convert to percentage

        # Predict the binary class label (0 or 1) for stroke risk
        risk = self.model.predict(x_scaled)[0]

        # Return both the probability (%) and the binary prediction
        return prob, risk
