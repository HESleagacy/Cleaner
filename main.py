import os
from cleaner import clear_folder  #Import function from the cleaner.py

#Get location
def get_junk_paths():
    return[
        os.getenv("TEMP"),
        r"C:\Windows\Temp",
        r"C:\Windows\Prefetch"
    ]

def main():
    print("Junk Cleaner by Sarva Dubey")
    paths = get_junk_paths()
    for path in paths:
        print("Cleaning at progress")
        if path and os.path.exists(path): #To avoid error
            print(f"Cleaning: {path}")
            files, folders, status = clear_folder(path)  # Call your function
            print(f"{status}")
            print(f"Files deleted: {files}")
            print(f"Folders deleted: {folders}\n")
        else:
         print("Skipped")

    print("Done")

if __name__ == "__main__":
   main() 