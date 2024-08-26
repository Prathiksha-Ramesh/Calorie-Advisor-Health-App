# Calorie Advisor Health App

This project is a Streamlit-based application that allows users to upload images of food, and then uses Google's Generative AI to analyze the food items in the image, calculate the total calories, and provide a detailed breakdown of the nutritional content. The app also advises whether the food is healthy based on the analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)
- [Contributing](#contributing)

## Overview

The Calorie Advisor Health App enables users to gain insights into the nutritional content of their meals by simply uploading a photo of their food. The app uses Google's Generative AI to analyze the image and provide an estimate of the total calories, along with a detailed breakdown of the nutritional components such as carbohydrates, fats, fibers, and sugars.

## Features

- **Image Upload**: Users can upload an image of their meal, and the app will display the image for review.
- **Calorie Estimation**: The app uses AI to analyze the food items in the image and estimate the total calorie count.
- **Nutritional Breakdown**: Provides a detailed breakdown of the nutritional content, including carbohydrates, fats, fibers, sugars, and other essential nutrients.
- **Health Advice**: The app advises whether the food is healthy based on the analysis.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/calorie-advisor-health-app.git
    cd calorie-advisor-health-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the root directory with the following content:

      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

    - Replace `your_google_api_key` with your actual Google API key.

## Usage

To run the application:

```bash
streamlit run app.py
```
## How It Works:

- **Upload Image**: Use the file uploader to upload an image of your meal (supported formats: JPG, JPEG, PNG).
- **Calorie Estimation**: Click the "Tell me about the total calories" button to process the image.
- **View Results**: The app will display the total calories and a detailed nutritional breakdown based on the image.

### Example:

- **Upload Image**: Choose an image of your meal and upload it using the file uploader.
- **Analyze Food**: Click the button to initiate the calorie estimation process.
- **Review Results**: The AI-generated response will provide a detailed analysis of the meal.

## Project Structure

- `app.py`: Main application file that handles the Streamlit interface and core functionality.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `.env`: Environment variables file (not included in the repository; must be created by the user).
- `images/`: Directory where example images might be stored (optional).

## Dependencies

The project uses the following dependencies:

- `streamlit`: For building the interactive user interface.
- `google.generativeai`: For integrating Google's Generative AI.
- `python-dotenv`: For managing environment variables.
- `Pillow`: For image processing and display.

For a full list of dependencies, please refer to the `requirements.txt` file.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
