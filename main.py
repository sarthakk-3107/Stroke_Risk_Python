import tkinter as tk
from data_loader import DataLoader
from model import StrokeRiskModel
from ui import StrokeRiskApp

def main():
    # Load and preprocess data from CSV file
    data_loader = DataLoader("stroke_risk_dataset.csv")
    X, X_scaled, y = data_loader.load_data()

    # Initialize and train the stroke risk prediction model
    model = StrokeRiskModel()
    model.train(X_scaled, y)

    # Create the main application window
    root = tk.Tk()

    # Instantiate the StrokeRiskApp GUI with feature names, model, and data loader
    app = StrokeRiskApp(root, list(X.columns), model, data_loader)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
