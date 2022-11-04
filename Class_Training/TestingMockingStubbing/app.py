import os


def rm(file_name: str) -> bool:
    print("in  function")
    if os.path.isfile(file_name):  ## TRUE!
        print("in IF!")
        os.remove(file_name)
        print("after remove!")
        return True
    return False


if __name__ == "__main__":
    file = input("What file would you like to remove? ")
    rm(file)
