# Resume Filtering with LLM-based Scoring
This project automates the resume screening process using Large Language Models (LLMs) via the Groq API. It helps recruiters and HR professionals streamline candidate evaluation by comparing resumes to a predefined job description, scoring them intelligently, and categorizing them into selected or rejected based on match relevance.

#  Features
 Automated Resume Parsing: Extracts text from PDF resumes using PyMuPDF.

 Text Cleaning Pipeline: Cleans and normalizes resume content for uniformity and model readability.

 LLM-Powered Scoring Engine: Utilizes Groq’s LLM (DeepSeek LLaMA 70B Distill) to intelligently evaluate resumes against job descriptions.

 Vacancy-Aware Filtering: Automatically selects the top resumes based on the number of vacancies parsed from the job description.

 Folder Management: Copies PDF files of selected and rejected resumes into separate directories for further use.

 Interactive Cleanup Tool: Option to delete files from key directories using a user-friendly terminal interface.

 Orchestrated Workflow: flow.py handles all preprocessing and filtering steps in a sequential pipeline.

#  Project Structure
├── src/

│   ├── pdf_to_txt_PyMuPDF.py   # Extracts raw text from PDF resumes

│   ├── txt_clean.py            # Cleans and normalizes extracted resume text

│   ├── brain.py                # Core logic: scoring resumes using Groq LLM

│   ├── delete.py               # File cleanup utility

│   └── flow.py                 # Pipeline runner (executes all steps)

├── data/

│   ├── resumes/                # Original PDF resumes

│   ├── raw_3/                  # Text extracted from PDFs

│   ├── cleaned/                # Cleaned text resumes

│   ├── selected/               # PDFs of top-ranked resumes

│   ├── rejected/               # PDFs of non-selected resumes

│   └── job_description.txt     # Job description used for filtering

#  How It Works
1) PDF Parsing: Resume PDFs from data/resumes/ are converted to .txt using PyMuPDF.

2) Text Cleaning: The raw text is cleaned to remove noise, normalize formatting, and enhance LLM input quality.

3) Job Description Analysis: The job description file is parsed to determine the number of vacancies.

4) LLM Scoring: Each cleaned resume is evaluated against the job description. A score out of 100 is returned.

5) Resume Selection: The top resumes (equal to the number of vacancies) are selected, and their PDFs are moved to selected/. The rest go to rejected/.

6) Optional Cleanup: delete.py allows users to clear folders interactively.

# 🛠️ Requirements
Python 3.8+

groq

PyMuPDF

#  Powered By
Groq - Ultra-fast inference of open-source LLMs

DeepSeek LLaMA 70B Distill - Model used for resume evaluation
