import os
import re


def search_files_in_directories(directories, regex_pattern, output_directory):
    pattern = re.compile(regex_pattern)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    def search_in_directory(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        matches = pattern.findall(content)
                        if matches:
                            output_file_path = os.path.join(output_directory, f"{file}_matches.txt")
                            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                                output_file.write(f"Matches in {file_path}:\n")
                                for match in matches:
                                    output_file.write(f"{match}\n")
                                output_file.write("\n")
                except (IOError, UnicodeDecodeError) as e:
                    print(f"Could not read file {file_path}: {e}")
    
    for directory in directories:
        if os.path.isdir(directory):
            search_in_directory(directory)
        else:
            print(f"{directory} is not a valid directory.")


