# 💼 SmartHire AI — Job Description Analyzer

SmartHire AI is an AI-powered job description analyzer built with Python, LangGraph, Pydantic, and Streamlit. It analyzes job descriptions, extracts important information, classifies jobs, identifies technical and soft skills, and generates a structured hiring report.

## ✨ Features

- **Information Extraction:** Extracts job title, company name, required experience, and required skills.
- **Job Classification:** Identifies job category and employment type.
- **Skill Analysis:** Separates technical and soft skills and highlights the top three skills.
- **Hiring Report:** Generates a structured report from the analysis.
- **Interactive UI:** Provides a clean, user-friendly Streamlit dashboard.
- **JSON Export:** Download the analysis report as a JSON file.
- **Input Validation:** Handles missing or invalid job descriptions gracefully.
- **LangGraph Workflow:** Processes the analysis through four connected nodes.

## 🛠️ Technologies Used

- Python
- LangGraph
- LangChain
- Groq API
- Pydantic
- Streamlit
- python-dotenv

## 📁 Project Structure

```text
SmartHire-AI/
├── app.py
├── graph.py
├── llm.py
├── nodes.py
├── schemas.py
├── state.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rohama789-blip/AI-Job-Analyzer.git
cd AI-Job-Description-Analyzer
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

Get your API key from the [Groq Console](https://console.groq.com/keys).

**Security:** Never upload your actual API key or `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🔄 How It Works

SmartHire AI uses a four-node LangGraph workflow:

1. **Information Extraction** — Extracts key job details.
2. **Job Classification** — Determines the job category and employment type.
3. **Skill Analysis** — Identifies technical skills, soft skills, and the top three skills.
4. **Hiring Report** — Combines the results into a structured report.

## 📤 Export Results

After analyzing a job description, users can review the extracted details, classifications, and skills, then download the generated hiring report in JSON format.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key |
| `GROQ_MODEL` | Groq model used for analysis |

## 🚀 Future Improvements

- Resume and job description matching
- Candidate-job compatibility scoring
- Missing skills identification
- Resume upload and analysis
- PDF report generation
- Deployment to Streamlit Community Cloud

## 📄 License

This project is intended for educational and demonstration purposes. Add a license file if you plan to distribute it publicly.
