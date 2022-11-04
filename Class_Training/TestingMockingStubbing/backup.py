import os


def rm(file_name: str) -> str:

    if os.remove(file_name):
        print("subba da bin ich!")
        return f"File {file_name} removed!"


if __name__ == "__main__":
    file = input("What file would you like to remove? ")
    rm(file)
