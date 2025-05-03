import tkinter as tk
from tkinter import ttk
from gui_components import create_input_fields
from predictor import handle_prediction

class StrokeRiskApp:
    def __init__(self, root, features, model, data_loader):
        # Initialize the GUI with root window, feature names, trained model, and data loader
        self.root = root
        self.features = features
        self.model = model
        self.data_loader = data_loader
        self.entries = {}  # Dictionary to store form inputs
        self.setup_ui()    # Build the UI on startup

    def setup_ui(self):
        # Set window properties
        self.root.title("Stroke Risk Predictor")
        self.root.geometry("550x650")
        self.root.configure(bg="#e0f7fa")
        self.root.resizable(False, False)

        # Define styling for buttons and labels
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background="#e0f7fa", foreground="#2c3e50")
        style.configure("Section.TLabel", font=("Segoe UI", 10), background="#e0f7fa", foreground="#555")

        # Header label
        header = ttk.Label(self.root, text="Stroke Risk Prediction", style="Header.TLabel")
        header.grid(row=0, columnspan=2, pady=(20, 5))

        # Instruction label
        instruction = ttk.Label(
            self.root,
            text="Enter Age, and check symptoms you experience:",
            style="Section.TLabel"
        )
        instruction.grid(row=1, columnspan=2, pady=(0, 10))

        # Dynamically create input fields based on feature list
        self.entries, next_row = create_input_fields(self.root, self.features)

        # Button to trigger prediction
        predict_btn = ttk.Button(
            self.root,
            text="Predict Stroke Risk",
            command=lambda: handle_prediction(
                self.entries,
                self.features,
                self.data_loader,
                self.model
            )
        )
        predict_btn.grid(row=next_row, columnspan=2, pady=(15, 5))

        # Footer label
        footer = ttk.Label(self.root, text="AI-Powered Stroke Risk Tool", style="Section.TLabel")
        footer.grid(row=next_row + 1, columnspan=2, pady=10)
