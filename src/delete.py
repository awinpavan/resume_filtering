import os
import shutil

# Folder paths
raw_3_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\raw_3"
rejected_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\rejected"
selected_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\selected"
resumes_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\resumes"
cleaned_folder = r"C:\Users\awinp\Documents\shiji_resume_filtering\data\cleaned"

# Function to delete files in a folder
def delete_files_in_folder(folder_path):
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        
        if not files:
            print(f"No files to delete in {folder_path}")
            return

        # Ask the user for confirmation
        print(f"\nFiles in {folder_path}:")
        for file in files:
            print(f"- {file}")

        confirm = input(f"\nDo you want to delete all files in {folder_path}? (y/n): ").strip().lower()
        if confirm == 'y':
            for file in files:
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted: {file}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Deleted directory: {file}")
        else:
            print("Deletion canceled.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to prompt user for which folder to delete files from
def delete_files_based_on_user_choice():
    while True:  # Infinite loop until the user decides to exit
        print("\nSelect a folder to delete files from:")
        print("1. raw_3 folder")
        print("2. rejected folder")
        print("3. selected folder")
        print("4. resumes folder")
        print("5. cleaned folder")
        print("6. Exit")

        choice = input("Enter the number corresponding to the folder: ").strip()

        if choice == '1':
            delete_files_in_folder(raw_3_folder)
        elif choice == '2':
            delete_files_in_folder(rejected_folder)
        elif choice == '3':
            delete_files_in_folder(selected_folder)
        elif choice == '4':
            delete_files_in_folder(resumes_folder)
        elif choice == '5':
            delete_files_in_folder(cleaned_folder)
        elif choice == '6':
            print("Exiting the program.")
            break  # Exit the loop and close the program
        else:
            print("Invalid choice. Please select a valid option (1-5).")

# Run the script
if __name__ == "__main__":
    delete_files_based_on_user_choice()
