def myFunc():
    print("Hello world!")


if __name__ == "__main__":  # __name__ will __main__main if it is running from mail file otherwise in main.y it will print __module__
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)


print("Hello")