import json

def find_index():
    with open('messages/index.json', 'r') as index_file:
        data = json.load(index_file)


    #Removing all None data
    data_to_remove = []
    for i in data.keys():
        if data[i] == None:
            data_to_remove.append(i)

    for i in data_to_remove:
        data.pop(i)

    #Removing all Unknown Participants
    data_to_remove = []
    for i in data.keys():
        if data[i] == f"Direct Message with Unknown Participant":
            data_to_remove.append(i)

    for i in data_to_remove:
        data.pop(i)

    new_data = dict((x, y) for y, x in data.items())

    #Adding all users to a list
    list_of_users = []
    for i in data.values():
        list_of_users.append(i[20:])


    return list_of_users, new_data



