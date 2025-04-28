def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)

    finally:    #We are using finally here cause only print will not do anything inside a fun
        print("I am inside finally")

main()