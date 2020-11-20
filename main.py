from functions import *


def main():
    print("Downloading..")
    # process the json file to download imgs
    process_json("res/data.json") #file containing urls of images to be saved
    print("Done. Find files in img/")


if __name__ == '__main__':
    main()
