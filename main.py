import pandas
import os
from scripts import index
import requests
import shutil

list_of_users = index.find_index()[0]
list_of_users.sort()
index_data = index.find_index()[1]


def message_with_user():
    for user in list_of_users:
        print(user)
    while True:
        dm_user_input = input("\nEnter the user you want to load the messages with\n>")

        if index_data.get(f"Direct Message with {dm_user_input}") is not None:
            file_index = "c" + index_data[f"Direct Message with {dm_user_input}"]
            break
        else:
            print("No messages with user.")

    # Reading the messages.csv file
    df = pandas.read_csv(f"messages/{file_index}/messages.csv")
    df = df[["Timestamp", "Contents", "Attachments"]]

    # Creating new .csv file
    with open(f"{dm_user_input}_messages.csv", 'w') as message_file:
        df.to_csv(f"{dm_user_input}_messages.csv")
    message_file.close()

    os.startfile(f"{dm_user_input}_messages.csv")


def attachments_with_user():
    for user in list_of_users:
        print(user)

    while True:
        attach_user_input = input("\nEnter the user you want to load the messages with\n>")

        if index_data.get(f"Direct Message with {attach_user_input}") is not None:
            file_index = "c" + index_data[f"Direct Message with {attach_user_input}"]
            break
        else:
            print("User does not exist")

    df = pandas.read_csv(f"messages/{file_index}/messages.csv")
    df = df[["Attachments"]]
    df.dropna(subset=['Attachments'], inplace=True)

    if user_input == 2:

        with open(f"{attach_user_input}_attachments.csv", 'w') as attachment_file:
            df.to_csv(f"{attach_user_input}_attachments.csv")
        attachment_file.close()

        os.startfile(f"{attach_user_input}_attachments.csv")

    if user_input == 3:

        urls = df.to_string()
        urls = urls.split(" ")
        urls[:] = [x for x in urls if x]
        urls.pop(0)
        continue_down = input(f"There are {len(urls)} images, do you want to download? Y/N\n>").upper()

        if continue_down == "Y":
            os.mkdir(f'{attach_user_input}_attachments')
            image_name_count = 0
            for url in urls:
                filename = f'image_{image_name_count}.png'
                res = requests.get(url, stream=True)
                if res.status_code == 200:
                    with open(f"{attach_user_input}_attachments/{filename}", 'wb') as file:
                        shutil.copyfileobj(res.raw, file)
                image_name_count = image_name_count + 1
        elif continue_down == "N":
            attachments_with_user()
        else:
            attachments_with_user()


while True:
    try:
        user_input = int(input(
            "1.Messages with specific user\n2.Attachments with specific user (Open as CSV of links)\n3.Attachments with specific user(Download to folder)\n4.Exit\n>"))
        break
    except ValueError:
        print("Enter 1,2,3,4 from the above choices")

if user_input == 1:
    message_with_user()

elif user_input == 2 or user_input == 3:
    attachments_with_user()

elif user_input == 4:
    exit()