import os
import re

def clean_resume_text(raw_text):
    if not isinstance(raw_text, str):
        return ""

    # 1. Basic cleanup
    text = raw_text
    text = re.sub(r'\r\n', '\n', text)             # Normalize Windows newlines to \n
    text = re.sub(r'\n+', '\n', text)               # Collapse multiple newlines to single
    text = re.sub(r'[ \t]+', ' ', text)             # Replace multiple spaces/tabs with single space
    text = re.sub(r' +\n', '\n', text)              # Remove spaces before newline
    text = re.sub(r'\n +', '\n', text)              # Remove spaces after newline
    text = text.replace('\u2022', '-')               # Replace bullets with hyphens
    text = re.sub(r'[^\x00-\x7F]+', '', text)       # Remove non-ASCII characters
    text = text.strip()

    # 2. Title-case the first line (usually name)
    lines = text.split('\n')
    if lines:
        lines[0] = lines[0].strip().title()
    text = '\n'.join(lines)

    # 3. Section headers you want to normalize and separate with blank line
    section_headers = [
        'experience', 'education', 'skills', 'projects',
        'certifications', 'contact', 'profile', 'summary',
        'accomplishments', 'hobbies', 'languages', 'links',
        'employment history', 'details'
    ]

    # 4. Build regex pattern to match any of these headers case-insensitive, as whole words
    # We use a regex group for all headers combined
    headers_pattern = r'\b(' + '|'.join(re.escape(h) for h in section_headers) + r')\b'

    # 5. Replace matches with a blank line + uppercase header
    # Use a function for re.sub replacement to preserve matched text case-insensitive
    def replace_header(match):
        header = match.group(1)
        return '\n\n' + header.upper()

    # 6. Apply replacement to whole text
    text = re.sub(headers_pattern, replace_header, text, flags=re.IGNORECASE)

    # 7. Finally, collapse any >2 newlines to max 2 for neatness
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 8. Strip leading/trailing whitespace again (just in case)
    text = text.strip()

    return text

# === STEP 2: Set input and output directories ===
input_dir = r'C:\Users\awinp\Documents\shiji_resume_filtering\data\raw_3'       # Folder with raw .txt resume files
output_dir = r'C:\Users\awinp\Documents\shiji_resume_filtering\data\cleaned'    # Folder to save cleaned .txt files

# Create output folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# === STEP 3: Process each .txt file ===
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Read raw resume
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as file:
            raw_text = file.read()

        # Clean the resume
        cleaned_text = clean_resume_text(raw_text)

        # Write the cleaned text to the output folder
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

print(f"✅ All resumes cleaned and saved to: '{output_dir}'")
