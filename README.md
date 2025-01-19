# LangChain FastAPI and Streamlit Integration

## Overview
This repository demonstrates how to create a powerful AI-powered application by integrating **LangChain**, **FastAPI**, **Streamlit**, and **Qwen (Ollama)** LLM. The project enables users to generate explanations and analyze the advantages and disadvantages of various topics through an intuitive API and user interface.

---

## Features
- **Dynamic Prompting**: Custom prompts to generate concise explanations and lists of pros/cons for any topic.
- **FastAPI Integration**: Seamless backend API for serving LLM-generated responses.
- **Streamlit Front-End**: A user-friendly interface for interacting with the AI model.
- **Environment Configuration**: Easy-to-use `.env` setup for managing API keys and environment variables.

---

## Installation
Follow these steps to set up and run the project:

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Pip
- A Qwen-compatible LLM (Ollama) installed and set up

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/akashverma55/ModelAPI
   cd ModelAPI
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.

4. **Run the FastAPI Server**:
   ```bash
   python app.py
   ```

5. **Run the Streamlit App**:
   ```bash
   streamlit run user.py
   ```

---

## File Structure
```
.
├── app.py              # FastAPI backend with LangChain integration
├── user.py             # Streamlit front-end for user interaction
├── requirements.txt    # Required Python dependencies
├── .env.example        # Example environment variable file
├── README.md           # Project documentation
```

---

## Usage
### Backend API
1. Start the FastAPI server using `python app.py`. The server will be accessible at `http://localhost:8000`.
2. Endpoints:
   - `/explanation`: Generates an explanation for the given topic.
   - `/adv&disadv`: Provides advantages and disadvantages of the given topic.

### Front-End
1. Start the Streamlit app using `streamlit run user.py`.
2. Enter a topic in the input fields to:
   - Get a concise explanation.
   - Analyze its advantages and disadvantages.

---

## Example
### Backend API Example
- **Endpoint**: `/explanation`
- **Request Body**:
  ```json
  {
      "input": {"topic": "Artificial Intelligence"}
  }
  ```
- **Response**:
  ```json
  {
      "output": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans."
  }
  ```

## Contact
Feel free to reach out for questions or suggestions:
- **Email**: your.akvakv150@gmail.com
- **LinkedIn**: (https://linkedin.com/in/akashkuverma)

