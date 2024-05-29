import streamlit as st
import openai
from PIL import Image
import io
import base64
from openai import OpenAI
import os


# Configure OpenAI API

openai.api_key = 'OPENAI_API_KEY'
llm = OpenAI(api_key='OPENAI_API_KEY')
#client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

def extract_text_and_elements(image):
    # Dummy implementation - replace with actual extraction logic
    return "Some extracted text and design elements"

def generate_prompt(extracted_text):
    # Create a detailed prompt based on extracted elements
    prompt = f"Generate an image of a menu for a French bar. The menu should be worn and slightly weathered. Include several sections for different drink categories.Take design inspiration as mentioned. {extracted_text}"
    return prompt

def generate_image(prompt):
    response = llm.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url

def analyze_images(image_urls):
    # Limit the number of images to process to 1
    limited_image_urls = image_urls[:1]
    
    messages = [
        {"role": "system", "content": "Describe the design elements of this image."},
    ]
    for url in limited_image_urls:
        messages.append({"role": "user", "content": f"![image]({url})"})

    response = llm.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=messages,
        max_tokens=300,
    )
    return response.choices[0].message.content

# Streamlit app
st.title("Designer Drinks & Wine Menu Generator")

# File uploader for restaurant history and old menus
uploaded_files = st.file_uploader("Upload restaurant history or old menus", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_files:
    image_urls = []
    for uploaded_file in uploaded_files:
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        st.write("File uploaded successfully!")
        
        # Save the uploaded image to a temporary file and get its URL
        with io.BytesIO() as output:
            uploaded_image.save(output, format="PNG")
            image_data = output.getvalue()
            image_url = "data:image/png;base64," + base64.b64encode(image_data).decode('utf-8')
            image_urls.append(image_url)

    # Analyze the uploaded images
    extracted_text = analyze_images(image_urls)
    st.write("Extracted Design Elements:", extracted_text)

    # Generate descriptive prompt
    prompt = generate_prompt(extracted_text)
    st.write("Generated Prompt:", prompt)

    # Generate menu image using OpenAI API
    if st.button("Generate Menu"):
        image_url = generate_image(prompt)
        st.image(image_url, caption="Generated Menu", use_column_width=True)