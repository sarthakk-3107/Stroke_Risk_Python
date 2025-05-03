import tkinter as tk

def create_input_fields(root, features):
    # Dictionary to store input widgets for each feature
    entries = {}
    row = 2  # Start placing widgets from row 2 (header rows occupy the top)

    # Loop through all features to create respective input widgets
    for feature in features:
        # Special handling for "age" since it requires a numeric text entry
        if feature.lower() == "age":
            # Create label for age
            label = tk.Label(root, text="Age:", font=("Arial", 10), bg="#f0f8ff")
            label.grid(row=row, column=0, sticky="w", padx=20, pady=2)

            # Create input field for age
            entry = tk.Entry(root, font=("Arial", 10), width=10)
            entry.grid(row=row, column=1, padx=10, pady=2)

            # Store the entry widget in the dictionary
            entries[feature] = entry
        else:
            # For binary features, use checkboxes with default unchecked (0)
            var = tk.IntVar(value=0)
            cb = tk.Checkbutton(root, text=feature, variable=var, font=("Arial", 10), anchor="w", bg="#f0f8ff")
            cb.grid(row=row, column=0, columnspan=2, sticky="w", padx=20, pady=2)

            # Store the IntVar (state of checkbox) in the dictionary
            entries[feature] = var

        # Move to the next row in the UI layout
        row += 1

    # Return dictionary of input elements and the next available row
    return entries, row
