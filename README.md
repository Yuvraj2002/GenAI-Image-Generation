# GenAI-Image-Generation
Generate images using Dall-e-3 with an option to upload images of your own as context to better fit your use case.
Sure, here is the updated README file with descriptions of the libraries used:

---

# Designer Drinks & Wine Menu Generator

This application generates a custom drinks and wine menu for a French bar based on uploaded images of restaurant history or old menus. The application leverages OpenAI's GPT-4 and DALL-E 3 models to analyze the design elements of the uploaded images and generate a new, visually appealing menu.

## Description

The application allows users to upload images of their restaurant history or old menus. It then extracts design elements from these images and uses this information to generate a prompt for creating a new menu image. The new menu is generated using OpenAI's DALL-E 3 model, providing a custom, visually appealing design.

## Code Explanation

### Libraries

- **streamlit**:
  - Used for creating the web application interface. It provides functions to create UI elements like file uploaders, buttons, and to display images and text.
  
- **openai**:
  - Provides access to OpenAI's models, including GPT-4 and DALL-E 3, for generating text and images based on provided prompts and inputs.

- **PIL (Python Imaging Library)**:
  - Used for opening, manipulating, and saving images in various formats. It helps in processing the uploaded images before sending them for analysis.

- **io**:
  - Provides core tools for working with streams, including in-memory streams, which are used here to temporarily hold image data.

- **base64**:
  - Used for encoding and decoding binary data to text format. In this app, it helps convert image data to base64 strings for processing and display.

- **os**:
  - Used to interact with the operating system, specifically for managing environment variables.

### Functions

- **extract_text_and_elements(image)**:
  - Dummy implementation to simulate extraction of text and design elements from the image.
  - Returns: A string containing the extracted text and design elements.

- **generate_prompt(extracted_text)**:
  - Creates a detailed prompt for generating a new menu image based on extracted text and design elements.
  - Parameters: `extracted_text` (string) - Text and design elements extracted from the uploaded image.
  - Returns: A string containing the detailed prompt.

- **generate_image(prompt)**:
  - Uses OpenAI's DALL-E 3 model to generate a new menu image based on the provided prompt.
  - Parameters: `prompt` (string) - Detailed prompt for generating the new menu image.
  - Returns: URL of the generated image.

- **analyze_images(image_urls)**:
  - Analyzes the design elements of the provided image URLs using OpenAI's GPT-4 model.
  - Parameters: `image_urls` (list) - List of image URLs to be analyzed.
  - Returns: A string containing the description of the design elements.

### Streamlit App

- **st.title("Designer Drinks & Wine Menu Generator")**:
  - Sets the title of the Streamlit app.

- **st.file_uploader("Upload restaurant history or old menus", type=["jpg", "png"], accept_multiple_files=True)**:
  - Allows users to upload images (JPG, PNG) of restaurant history or old menus.

- **if uploaded_files**:
  - Checks if any files have been uploaded.
  - Iterates through each uploaded file to display the image and save it to a temporary file.

- **analyze_images(image_urls)**:
  - Analyzes the uploaded images to extract design elements.
  - Displays the extracted design elements in the app.

- **generate_prompt(extracted_text)**:
  - Generates a detailed prompt based on the extracted design elements.
  - Displays the generated prompt in the app.

- **if st.button("Generate Menu")**:
  - Generates a new menu image when the button is clicked.
  - Displays the generated menu image in the app.
