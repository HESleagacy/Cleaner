import os

def clear_folder(path: str):
    deleted_files = 0       #Counts deleted files
    deleted_folders = 0     #Counts deleted folders

    if not os.path.exists(path):
      return (0, 0, "Path not found")
    try: #Gather all files along with folders from bottom to top
        for root, dirs, files in os.walk(path, topdown=False):
            for file in files: #Deletes Files
                file_path = os.path.join(root, file) #Joint Paths
                try:
                    os.remove(file_path) #Delete the file
                    deleted_files += 1
                except Exception as e:
                    print("Cant delete your files")  

            for dir in dirs:
                dir_path = os.path.join(root, dir) #Joint Paths
                try: #Delete Folders
                    os.rmdir(dir_path)  #Remove Directory path
                    deleted_folders += 1
                except Exception as e:
                    print("Cant delete your files")

        return(deleted_files, deleted_folders, "Cleaned")

    except Exception as e:
        return(0,0,"Permission not granted")                 



