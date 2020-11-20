from functions import *


def main():
    print("Downloading..")
    # make res folder, if not already created
    if not os.path.exists("res"):
        os.makedirs("res")
    process_json("res/data.json") #json-like file containing urls of images to be saved


if __name__ == '__main__':
    main()
