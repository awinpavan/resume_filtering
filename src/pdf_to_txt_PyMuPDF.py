import os
import fitz  # PyMuPDF

# Folders
pdf_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\resumes"
output_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\raw_3"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(pdf_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        txt_filename = filename.replace(".pdf", ".txt")
        txt_path = os.path.join(output_folder, txt_filename)

        if os.path.exists(txt_path):
            print(f"⏭️ Skipping (already converted): {txt_filename}")
            continue

        print(f"🔄 Extracting using PyMuPDF: {filename}")
        try:
            doc = fitz.open(pdf_path)
            full_text = ""
            for page in doc:
                full_text += page.get_text()

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(full_text)

        except Exception as e:
            print(f"❌ Error converting {filename}: {e}")

print("✅ Done! Extracted with PyMuPDF (fitz).")
