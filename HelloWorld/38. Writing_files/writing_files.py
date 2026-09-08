# writing files .txt. .json .csv

txt_data = "I like pizza"

file_path = "HelloWorld/38. Writing_files/ output.txt"

with open(file=file_path, mode="w") as file:  #se volessi aggiungere scritte al file esistente, dovrei usare "a"
    file.write(txt_data)
    print(f"txt file {file_path}' wass created")