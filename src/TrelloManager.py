import requests

# we may need use another method to not expose the user's token
api_key = "your_api_key"
token = "your_token"

BASE_URL = "https://api.trello.com/1"
def get_full_board_info(short_board_id):
    url = f"{BASE_URL}/boards/{short_board_id}"
    query = {
        'key': api_key,
        'token': token
    }
    response = requests.get(url, params=query)

    if response.status_code == 200:
        board_info = response.json()
        print(f"Board Name: {board_info['name']}")
        print(f"Full Board ID: {board_info['id']}")
        return board_info['id']
    else:
        print(f"failed: {response.status_code}")
        print(response.text)

def get_lists(board_id):
    url = f"{BASE_URL}/boards/{board_id}/lists"
    query = {
        'key': api_key,
        'token': token
    }
    response = requests.get(url, params=query)

    list_id = []
    if response.status_code == 200:
        lists = response.json()
        for lst in lists:
            list_id.append(lst['id'])
            print(f"List Name: {lst['name']}, List ID: {lst['id']}")
    else:
        print(f"Failed fetching lists: {response.status_code}")
        print(response.text)

    return list_id

def create_card(list_id, name, desc=""):
    url = f"{BASE_URL}/cards"
    query = {
        'key': api_key,
        'token': token,
        'idList': list_id,
        'name': name,
        'desc': desc
    }
    response = requests.post(url, params=query)

    if response.status_code == 200:
        print("Successfully created!")
        print(response.json())
    else:
        print(f"Failed: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # go to your target workspace and board, you will see a short id in your url
    # example: https://trello.com/b/{short_board_id}/{board_name}
    short_board_id = "short_board_id"
    full_board_id = get_full_board_info(short_board_id)
    # to simply test, I just chose the first list to add a new card
    list_id = get_lists(full_board_id)
    create_card(list_id[0],"new to-do", "This is a new task created by the bot")
