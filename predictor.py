import pandas as pd
from tkinter import messagebox

def handle_prediction(entries, features, data_loader, model):
    try:
        input_data = []

        # Extract values from GUI input fields
        for feature in features:
            val = entries[feature].get()

            # Raise an error if any input is missing
            if val == "":
                raise ValueError(f"Missing input for: {feature}")

            # Convert the input to float (for numeric and binary inputs)
            input_data.append(float(val))

        # Convert user input into a DataFrame with proper column names
        input_df = pd.DataFrame([input_data], columns=features)

        # Scale the input using the same scaler used during training
        x_scaled = data_loader.transform_input(input_df)

        # Make prediction using the trained model
        prob, risk = model.predict(x_scaled)

        # Display the result in a message box
        messagebox.showinfo("Prediction Result", f"Stroke Risk: {prob:.2f}%\nAt Risk: {'Yes' if risk else 'No'}")

    except Exception as e:
        # Handle and display any errors (e.g., invalid input or prediction issues)
        messagebox.showerror("Error", str(e))
