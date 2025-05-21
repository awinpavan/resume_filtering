# 📄 Resume Filtering with LLM-based Scoring

This project automates the resume screening process using Large Language Models (LLMs) via the **Groq API**. It helps recruiters and HR professionals streamline candidate evaluation by comparing resumes to a predefined job description, intelligently scoring them, and categorizing them as **selected** or **rejected** based on relevance.

---

## ✨ Features

- **Automated Resume Parsing**  
  Extracts text from PDF resumes using PyMuPDF.

- **Text Cleaning Pipeline**  
  Cleans and normalizes resume content for uniformity and model readability.

- **LLM-Powered Scoring Engine**  
  Utilizes Groq’s LLM (DeepSeek LLaMA 70B Distill) to evaluate resumes intelligently.

- **Vacancy-Aware Filtering**  
  Automatically selects the top resumes based on the number of vacancies in the job description.

- **Folder Management**  
  Copies PDF files of selected and rejected resumes into separate directories.

- **Interactive Cleanup Tool**  
  Delete files from directories using a user-friendly terminal interface.

- **Orchestrated Workflow**  
  `flow.py` handles all preprocessing and filtering steps in a sequential pipeline.

---

## 🧱 Project Structure

├── src/

│ ├── pdf_to_txt_PyMuPDF.py # Extracts raw text from PDF resumes

│ ├── txt_clean.py # Cleans and normalizes extracted resume text

│ ├── brain.py # Core logic: scoring resumes using Groq LLM

│ ├── delete.py # File cleanup utility

│ └── flow.py # Pipeline runner (executes all steps)

├── data/

│ ├── resumes/ # Original PDF resumes

│ ├── raw_3/ # Text extracted from PDFs

│ ├── cleaned/ # Cleaned text resumes

│ ├── selected/ # PDFs of top-ranked resumes

│ ├── rejected/ # PDFs of non-selected resumes

│ └── job_description.txt # Job description used for filtering


---

## ⚙️ How It Works

1. **PDF Parsing**  
   Resume PDFs from `data/resumes/` are converted to `.txt` using PyMuPDF.

2. **Text Cleaning**  
   Raw text is cleaned to remove noise, normalize formatting, and improve LLM input.

3. **Job Description Analysis**  
   Parses the job description file to determine the number of vacancies.

4. **LLM Scoring**  
   Each cleaned resume is evaluated against the job description. A score out of 100 is generated.

5. **Resume Selection**  
   Top resumes (equal to number of vacancies) are selected and moved to `selected/`. Others go to `rejected/`.

6. **Optional Cleanup**  
   `delete.py` lets users clear folders interactively.

---

## 🛠️ Requirements

- Python 3.8+
- `groq`
- `PyMuPDF`

---

## 🚀 Powered By

- **Groq** — Ultra-fast inference of open-source LLMs  
- **DeepSeek LLaMA 70B Distill** — Used for resume evaluation

---

