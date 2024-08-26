import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Generative AI client
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input_prompt, image_data):
    # Initialize the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Combine the prompt and image data into a list for content generation
    inputs = [input_prompt, image_data]
    
    # Generate content using the inputs
    response = model.generate_content(inputs)
    
    # Return the generated text
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,
            'data': bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

# Set up Streamlit app configuration
st.set_page_config(page_title="Calorie Advisor Health App")

# File uploader widget
uploaded_file = st.file_uploader('Choose an image....', type=['jpg', 'jpeg', 'png'])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Button to trigger calorie estimation
submit = st.button('Tell me about the total calories')

# Input prompt for the AI model
input_prompt = """
You are an expert nutritionist. You need to analyze the food items in the image and calculate 
the total calories. Also, provide the details of every food item with calorie intake in the following format:

1. Item 1 - number of calories
2. Item 2 - number of calories
------
Finally, mention whether the food is healthy or not, and provide the percentage split 
of the ratio of carbohydrates, fats, fibers, sugars, and other essential nutrients.
"""

if submit and uploaded_file is not None:
    # Process the uploaded image
    image_data = input_image_setup(uploaded_file)
    
    # Get the AI model response
    try:
        response = get_gemini_response(input_prompt, image_data)
        st.header('The Response is:')
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
