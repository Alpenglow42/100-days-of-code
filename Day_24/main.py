# file = open("my_text.txt") # manually open until Manually close
# with open("my_text.txt") as file: # closes file after finsihed getting info
#     contents = file.read()
#     print(contents)
# # file.close() # manually closes file

with open("my_text.txt", mode="a") as file: # mode=w for write, mode=a for append
    file.write("\nI also like meditation") # \n add to new line

with open("new_file.txt",mode="w") as file: # creates new file only when in write mode
    #and new file doesn't exist
    file.write("New Text")