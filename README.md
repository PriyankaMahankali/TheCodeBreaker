# Code Breaker Application - README

## Overview
The **Code Breaker** application is a Python-based graphical user interface (GUI) built with Tkinter, designed to decode encrypted text using frequency analysis. The program takes two inputs: plain English text and an encrypted message. It then generates a mapping based on relative letter frequencies and provides the decoded message. The app also provides visualizations of letter frequency distributions through pie charts. This app was developed as a submission for the WISE program conducted jointly by BVRIT Hyderabad. 

This application includes:
- An animated background to enhance the user interface.
- An interactive decoding interface for text input.
- Pie chart visualizations for letter frequency comparison.
- A decoded message output with the letter-to-letter mapping.

## Features
- **Animated Background**: The app displays an animated GIF that adds a dynamic touch to the interface.
- **Input Section**: Users can input plain and encrypted messages for decoding.
- **Pie Chart Visualization**: After deciphering, the app generates pie charts showing the frequency distribution of letters in both the plain and encrypted text.
- **Mapping Display**: The app provides a mapping of letters based on frequency comparison between the input texts.
- **Decoded Message**: The decoded message is shown based on the calculated letter mapping.
- **Help Section**: A detailed help dialog explaining how to use the app is available.
- **Exit Option**: The user can exit the application from both the main screen and the output section.

## How to Use
1. **Start the Application**:
   - Open the application and click the "Start" button.
   - This will open the input section where you can enter the plain and encrypted text.

2. **Input Text**:
   - Enter the plain English message in the first input box.
   - Enter the encrypted message in the second input box.

3. **Decipher the Message**:
   - Click the "Decipher" button to process the input.
   - The app will compare the letter frequencies of the two texts and provide a mapping, along with the decoded message.

4. **View Results**:
   - The application will display pie charts visualizing the letter frequency distributions of both the plain and encrypted texts.
   - The decoded message will be displayed based on the letter mappings.

5. **Help**:
   - Click the "Help" button on the main screen to view detailed instructions on how to use the app.

6. **Exit the Application**:
   - You can exit the application at any time by clicking the "Exit" button.

## Requirements
- Python 3.x
- Tkinter (included with Python standard library)
- Pillow (for handling images and GIFs)
- Matplotlib (for generating pie charts)

### Install dependencies:
```bash
pip install pillow matplotlib
```

## File Structure
- `1_AGct0ZJuD8ZHV1jMnvJlIw.gif`: Animated GIF used as the background animation.
- `DataBreach.png`: Background image for the input section.
- `op_bg.png`: Background image for the output section.
- `main.py`: The main Python script containing the application logic.

## Classes and Functions
### `CustomDialog`
A custom dialog box used for displaying messages like plain text, encoded text, decoded message, and mapping.

### `AnimatedApp`
The main class responsible for running the application. It includes:
- **Animation**: The background animation functionality.
- **Input Section**: The functionality to input text and start the decipher process.
- **Output Section**: The functionality to display the results of the decoding, including the letter frequency pie charts and decoded message.

### `show_custom_dialog()`
Displays a custom dialog box with a title and message passed to it.

### `rel_freq()`
Calculates the relative frequency of each letter in a given text.

### `decipher()`
Performs the frequency analysis and decodes the encrypted message by mapping the most frequent letters in the encrypted text to the most frequent letters in the plain text.

### `plot_pie_chart()`
Generates a pie chart visualizing the relative frequencies of letters in the text.
