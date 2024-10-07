# Text To Image Generator

This project is a **Text-to-Image Generator** application built using Python's `Tkinter` for the graphical user interface (GUI) and the **Stable Diffusion** model for generating images from text. The app allows users to enter a description, click a button, and generate a corresponding image.

## Features
- Simple and easy-to-use GUI built with `Tkinter`.
- Integration with the **Stable Diffusion** model for high-quality image generation.
- Ability to save generated images locally.
- Responsive layout that adjusts based on window size.

## Prerequisites
To run this project, you will need:
- **Python 3.7+**
- Access to a Stable Diffusion API or local model (e.g., via Hugging Face, OpenAI, or another service)
- The following Python libraries:
  - `Tkinter`
  - `PIL` (Pillow for image handling)
  - `requests` (if using an API for Stable Diffusion)
  - `torch` (if using a local model)
  - `transformers` (for handling Stable Diffusion model)

## Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/Sreejith2003/Text_To_Image.git
    ```

2. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Stable Diffusion:**

   - If using a local model, download it (e.g., from Hugging Face).
   - If using an API, ensure you have the correct API key and access.

4. **Run the application:**

    ```bash
    python main.py
    ```

## Usage

1. Open the app and enter a description or text prompt in the input box.
2. Click the "Generate Image" button.
3. The generated image will be displayed in the app window.
4. You can save the image by clicking the "Save" button.

Happy Reading :)
