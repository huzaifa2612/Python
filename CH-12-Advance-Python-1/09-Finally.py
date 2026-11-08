def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside of finally")   # Finally chalta hi chlta ha chahy Try block mai function return ho rha ho


main()