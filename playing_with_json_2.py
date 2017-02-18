import requests
import json


def print_json_object(json_object):
    print("Original: ")
    print(json_object)

    print()
    # print("----------------------------")

    print("Clean: ")
    print("name: " + json_object["name"])
    print("class: " + json_object["recclass"])
    print("longitude: " + json_object["reclong"])
    print("latitude: " + json_object["reclat"])
    print("year: " + json_object["year"])


def main():
    # url = "https://data.nasa.gov/resource/y77d-th95.json"
    # queried based on a mass > 5,000,000, for a smaller dataset
    url = "https://data.nasa.gov/resource/y77d-th95.json?$where=mass>5000000"

    response = requests.get(url)

    if response.status_code == 200:
        # following line puts json file into a python list
        data = response.json()

    # exporting python list to txt file
    # with open('data.txt', 'w') as outfile:
    #     json.dump(data, outfile)

    # iterating and printing the dataset
    for i in range(len(data)):
        print_json_object(data[i])
        print("\n----------------------------\n")


if __name__ == '__main__':
    main()
