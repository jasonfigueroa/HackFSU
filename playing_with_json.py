import requests
import json


def main():
    url = "https://data.nasa.gov/resource/y77d-th95.json"

    response = requests.get(url)

    if response.status_code == 200:
        # following line puts json file into a python list
        data = response.json()

    # exporting python list to txt file
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

    # assigning first item in list to dictionary (key value pair)
    item1 = data[0]

    # this print is unformatted & difficult to read
    print(item1)

    # accessing a key value pair from item1
    print("\n" + item1["name"])


if __name__ == '__main__':
    main()
