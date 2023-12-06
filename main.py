import pandas
import os
from scripts import index


directory_list = os.listdir("messages")


list_of_users = index.main()[0]
index_data = index.main()[1]

for i in list_of_users:
    print(i)


while True:
    user_input = input(">")

    if index_data.get(f"Direct Message with {user_input}") is not None:
        file_index = "c"+index_data[f"Direct Message with {user_input}"]
        break
    else:
        print("No messages with user.")

#Reading the messages.csv file
df = pandas.read_csv(f"messages/{file_index}/messages.csv")
df = df[["Timestamp", "Contents", "Attachments"]]

#Creating new .csv file
with open(f"{user_input}_messages.csv", 'w') as message_file:
    df.to_csv(f"{user_input}_messages.csv")
message_file.close()

os.startfile(f"{user_input}_messages.csv")