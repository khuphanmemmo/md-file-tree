import os
import pathlib

def generate_markdown_list(directory_path):
    """
    Creates a Markdown list of files and directories.
    """
    output = ""
    # Use pathlib to get the directory name
    directory_name = pathlib.Path(directory_path).name
    
    # Title for the directory
    output += f"- 📂 **`{directory_name}`**\n"
    
    # os.walk is great for traversing directory trees
    # The topdown=True argument makes it walk from top to bottom
    for root, dirs, files in os.walk(directory_path, topdown=True):
        # Lọc các thư mục ẩn và node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        # Lọc các file ẩn
        files = [f for f in files if not f.startswith('.')]
        # Calculate the indentation level for the current item
        level = root.replace(directory_path, '').count(os.sep)
        indentation = "  " * (level + 1)
        
        # Sort directories and files for a cleaner output
        dirs.sort()
        files.sort()
        
        # Add subdirectories to the output
        for d in dirs:
            dir_path = os.path.join(root, d)
            # Exclude dotfiles and directories (e.g., .git) and 'node_modules'
            if not d.startswith('.') and d != 'node_modules':
                # Use a different icon for subdirectories
                relative_dir_path = os.path.relpath(dir_path, directory_path)
                output += f"{indentation}- 📁 **`{d}`**\n"
        
        # Add files to the output
        for f in files:
            file_path = os.path.join(root, f)
            # Exclude dotfiles (e.g., .DS_Store)
            if not f.startswith('.'):
                relative_file_path = os.path.relpath(file_path, directory_path)
                # Markdown link for files
                output += f"{indentation}- 📄 [`{f}`]({relative_file_path})\n"

    return output

if __name__ == "__main__":
    # Get the current working directory
    current_directory = os.getcwd()
    # Generate the Markdown list
    markdown_output = generate_markdown_list(current_directory)
    # Print the result
    print(markdown_output)