import subprocess
import os
import sys  # ✅ Import sys to use the correct Python interpreter

def run_script(script_name):
    script_path = os.path.join('src', script_name)
    print(f"\n▶️ Running: {script_name}")
    try:
        # ✅ Use the current Python interpreter instead of plain 'python'
        subprocess.run([sys.executable, script_path], check=True)
        print(f"✅ Finished: {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {script_name}: {e}")
        exit(1)

if __name__ == "__main__":
    print("🚀 Starting Resume Processing Flow...\n")

    run_script('pdf_to_txt_PyMuPDF.py')  # Step 1: Convert PDFs to text
    run_script('txt_clean.py')           # Step 2: Clean the text resumes
    run_script('brain.py')               # Step 3: Perform filtering or classification

    print("\n🎯 All steps completed successfully.")
