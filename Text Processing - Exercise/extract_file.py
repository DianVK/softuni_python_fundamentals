file_url = input().split(".")

extension = file_url[1]
file_url.remove(extension)
search_file_name = file_url[0].split("\\")
file_name = search_file_name[-1]

print(f"File name: {file_name}\nFile extension: {extension}")