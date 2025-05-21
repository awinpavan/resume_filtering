import os
import shutil
import re
from groq import Groq

# Ensure your GROQ_API_KEY is set as an environment variable
client = Groq(api_key="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")

# Folder paths
cleaned_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\cleaned"
resumes_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\resumes"  # Correct folder for PDFs
selected_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\selected"
rejected_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\rejected"
job_description_path = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\job_description.txt"

# Create selected and rejected folders if they don't exist
os.makedirs(selected_folder, exist_ok=True)
os.makedirs(rejected_folder, exist_ok=True)

# Load the job description
with open(job_description_path, 'r', encoding='utf-8') as f:
    job_description = f.read()

# Function to extract number of vacancies from the job description
def extract_vacancies_from_job_description(job_description):
    # Use regex to find the number of vacancies after "Vacancies"
    match = re.search(r"Vacancies\s*[:\-]?\s*(\d+)", job_description)
    if match:
        return int(match.group(1))
    else:
        print("Vacancies section not found in the job description.")
        return 0  # Default to 0 if not found

# Extract the number of vacancies from the job description
vacancies_count = extract_vacancies_from_job_description(job_description)
print(f"Number of vacancies: {vacancies_count}")

# Function to compare resume with job description
def compare_resume_with_job(resume_text, job_description):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an HR expert who recruits people for the job described. Please evaluate the resume's match to the job description. Provide a score out of 100 based on the following criteria:\n"
                           "Example to look into field when comparing the resume to the job description are: \n"
                           "1. Relevant experience that matches or can be of use when comparing with the job description.\n"
                           "2. Relevant skills that matches or can be of use with when comparing with the job description .\n"
                           "3. Educational background besides higher secondary and secondary education that compliments with the job description.\n"
                           "4. Any additional skill sets or extra information that are of use when comparing with the job description.\n"
                           "5. Any sort of hobbies mentioned in the resume is welcome and appriciated. \n"
                           "post note: Please do not round the score. The score should be given as a precise value, not rounded to the nearest whole number, it can be given integer values while scoring."
            },
            {
                "role": "user",
                "content": f"Job Description: {job_description}\n\nResume: {resume_text}",
            }
        ],
        model="deepseek-r1-distill-llama-70b",
    )
    
    # Extracting the numeric score from the response (assuming the model returns it in this format: 'Score: 20/100')
    message = chat_completion.choices[0].message.content
    match = re.search(r"Score:\s*(\d+)", message)  # Extract the number after "Score:"
    if match:
        return int(match.group(1))  # Convert the score to an integer
    else:
        return 0  # Return 0 if no score is found
    []

# Store resumes and their scores
resume_scores = []

# Iterate through all resumes in raw_3 folder
for filename in os.listdir(cleaned_folder):
    if filename.lower().endswith(".txt"):
        resume_txt_path = os.path.join(cleaned_folder, filename)

        # Read resume content
        with open(resume_txt_path, 'r', encoding='utf-8') as file:
            resume_text = file.read()

        # Compare resume with job description
        score = compare_resume_with_job(resume_text, job_description)
        print(f"Resume: {filename}, Score: {score}")

        # Add the resume and its score to the list
        resume_scores.append((filename, score))

# Sort the resumes by score in descending order
resume_scores.sort(key=lambda x: x[1], reverse=True)

# Select the top `vacancies_count` resumes
selected_resumes = resume_scores[:vacancies_count]
rejected_resumes = resume_scores[vacancies_count:]

# Move the selected resumes' corresponding PDFs to the selected folder
for resume_file, score in selected_resumes:
    resume_pdf = resume_file.replace(".txt", ".pdf")
    resume_pdf_path = os.path.join(resumes_folder, resume_pdf)  # Correct PDF folder path

    # Check if the PDF already exists in the selected folder to avoid duplicates
    if os.path.exists(resume_pdf_path):  # Ensure the PDF exists in the resumes folder
        if not os.path.exists(os.path.join(selected_folder, resume_pdf)):
            shutil.copy(resume_pdf_path, os.path.join(selected_folder, resume_pdf))
            print(f"Selected Resume PDF: {resume_pdf} copied to selected folder.")
        else:
            print(f"Resume PDF {resume_pdf} is already selected.")
    else:
        print(f"PDF for {resume_pdf} not found in the resumes folder.")

# Optionally: Move rejected resumes PDF'S to the selected folder 
for resume_file, score in rejected_resumes:
    resume_pdf = resume_file.replace(".txt", ".pdf")
    resume_pdf_path = os.path.join(resumes_folder, resume_pdf)  # Correct PDF folder path

    # Check if the PDF already exists in the rejected folder to avoid duplicates
    if os.path.exists(resume_pdf_path):  # Ensure the PDF exists in the resumes folder
        if not os.path.exists(os.path.join(rejected_folder, resume_pdf)):
            shutil.copy(resume_pdf_path, os.path.join(rejected_folder, resume_pdf))
            print(f"Selected Resume PDF: {resume_pdf} copied to selected folder.")
        else:
            print(f"Resume PDF {resume_pdf} is already selected.")
    else:
        print(f"PDF for {resume_pdf} not found in the resumes folder.")
