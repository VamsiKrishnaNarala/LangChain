# LangChain

# Chatbot Application

## Overview
This project is a chatbot application built using LangChain and OpenAI's GPT model. The application takes user input and generates responses based on predefined prompts. It is developed using Python and Streamlit for the UI.

## Features
- User-friendly chatbot interface using Streamlit
- Sequential chains of prompts to generate responses
- Conversation memory using LangChain
- OpenAI API integration for generating responses

## File Structure
- `app.py`: Main script for the chatbot interface.
- `app1.py` - `app6.py`: Different versions of the chatbot application with incremental features such as memory and additional prompt templates.
- `key.py`: Stores the OpenAI API key (replace it with your own key).
- `requirements.txt`: Lists required dependencies for the project.

## Setup Instructions
### Prerequisites
Ensure you have Python installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd Langchain
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the OpenAI API key:
   - Replace the placeholder key in `key.py` with your own valid OpenAI API key.

## Running the Application
Execute the following command to run the chatbot:
```bash
streamlit run app.py
```
Replace `app.py` with any other version like `app6.py` if you want additional features like conversation memory.

## Dependencies
- LangChain
- OpenAI
- Streamlit
- LangChain Community

## Notes
- Ensure you have a valid OpenAI API key for the chatbot to function correctly.
- Modify the prompt templates in the `appX.py` files to customize the chatbot responses.

## License
This project is open-source. Feel free to modify and use it as per your requirements.

## Author
Narala Vamsi Krishna

