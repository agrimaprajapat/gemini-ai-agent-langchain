# Gemini AI Agent with Tool Calling

A simple AI Agent built using **LangChain**, **Google Gemini 2.0 Flash**, and **Streamlit**. The agent can answer general questions and use custom tools whenever needed.

## Features

- Google Gemini 2.0 Flash integration
- LangChain Tool Calling Agent
- Calculator Tool for mathematical operations
- Word Counter Tool for counting words in text
- Streamlit-based user interface
- Automatic tool selection by the agent

## Tools

### 1. Calculator Tool
Performs mathematical calculations.

**Example Input**
```text
2 + 5 * 10
```

**Output**
```text
52
```

### 2. Word Counter Tool
Counts the number of words in a given text.

**Example Input**
```text
Machine Learning is awesome
```

**Output**
```text
Total Words: 4
```

## Technologies Used

- Python
- LangChain
- Google Gemini API
- Streamlit
- python-dotenv

## Project Structure

```text
project/
│
├── app.py
├── tools.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd project
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

## Example Queries

- What is Machine Learning?
- Calculate 45 * 12 + 100
- Count words in "Artificial Intelligence is transforming the world"
- Explain Deep Learning
- Calculate (25 + 15) * 4

## Future Improvements

- Add more custom tools
- Web Search Integration
- Chat History Support
- Memory-enabled Agents
- Multi-Agent Systems
- File Upload Support

## Author

Agrima Prajapat