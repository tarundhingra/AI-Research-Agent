# AI Research Agent

An AI-powered research automation application that generates structured research reports from user-defined topics using LangChain agents, Google Gemini, Tavily Search, web scraping, and Streamlit.

The project follows a multi-agent workflow where one agent searches the web, another agent scrapes relevant content, a writer chain generates a detailed research report, and a critic chain evaluates the quality of the final output.

---

## Features

* Search the web for recent and reliable information using Tavily Search API
* Scrape relevant web pages for deeper research content
* Generate structured research reports using Google Gemini
* Evaluate generated reports using an AI critic chain
* Streamlit-based user interface for easy interaction
* Download generated research reports as text files
* Displays search results, scraped content, final report, and critic feedback

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini API
* Tavily Search API
* BeautifulSoup
* Requests
* python-dotenv

---

## Project Structure

```text
AI-Research-Agent/
│
├── app.py              # Streamlit UI
├── agent.py            # LLM setup, search agent, reader agent, writer chain, critic chain
├── pipeline.py         # Main research pipeline
├── tools.py            # Tavily web search and URL scraping tools
├── requirements.txt    # Python dependencies
├── .env                # API keys, not pushed to GitHub
└── README.md
```

---

## How It Works

The application follows a four-step research pipeline:

### 1. Search Agent

The search agent takes a user-defined topic and searches the web for recent and reliable information using Tavily Search.

### 2. Reader Agent

The reader agent selects the most relevant URL from the search results and scrapes the page content for deeper research.

### 3. Writer Chain

The writer chain uses the gathered research content to generate a structured research report with:

* Introduction
* Key Findings
* Conclusion
* Sources

### 4. Critic Chain

The critic chain reviews the generated report and provides:

* Score out of 10
* Strengths
* Areas to Improve
* One-line verdict

---

## Installation

Clone the repository:

```bash
git clone https://github.com/tarundhingra/AI-Research-Agent.git
cd AI-Research-Agent
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

For Windows:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory and add your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit
langchain
langchain-core
langchain-google-genai
python-dotenv
tavily-python
beautifulsoup4
requests
rich
```

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal.

---

## Usage

1. Enter a research topic in the input field.
2. Click on **Generate Research Report**.
3. View the generated report in the **Final Report** tab.
4. Review AI feedback in the **Critic Feedback** tab.
5. Check raw search results and scraped content in separate tabs.
6. Download the report as a `.txt` file.

---

## Example Topics

* Impact of AI on healthcare
* Future of renewable energy in India
* Role of Generative AI in education
* Cybersecurity trends in 2026
* Applications of AI agents in business automation

---

## Deployment on Streamlit Cloud

### 1. Push Project to GitHub

Make sure your repository contains:

```text
app.py
agent.py
pipeline.py
tools.py
requirements.txt
README.md
```

Do not push your `.env` file.

Add a `.gitignore` file:

```txt
.env
.venv/
__pycache__/
*.pyc
```

### 2. Deploy on Streamlit Community Cloud

1. Go to Streamlit Community Cloud.
2. Sign in with GitHub.
3. Click **New App**.
4. Select your repository.
5. Select the branch.
6. Set the main file path as:

```text
app.py
```

7. Click **Deploy**.

### 3. Add Secrets

In Streamlit Cloud, go to:

```text
App Settings → Secrets
```

Add:

```toml
GOOGLE_API_KEY = "your_google_api_key_here"
TAVILY_API_KEY = "your_tavily_api_key_here"
```

---

## Important Note

Before deployment, remove any test function calls from `tools.py`, such as:

```python
print(web_search.invoke("what is the recent news of war"))
print(scrape_url.invoke("https://menza.ai/"))
```

These lines run automatically when the file is imported and may slow down or break the Streamlit app.

---

## Future Improvements

* Add PDF export for generated reports
* Add support for multiple scraped sources
* Store previous research reports in a database
* Add user authentication
* Improve report citation formatting
* Add source ranking based on reliability
* Add support for follow-up questions on generated reports

---

## Author

**Tarun Dhingra**

* GitHub: [tarundhingra](https://github.com/tarundhingra)
* LinkedIn: [Tarun Dhingra](https://www.linkedin.com/in/tarundhingra/)
