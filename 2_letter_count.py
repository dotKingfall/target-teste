def main():
    check = ['a', 'A']
    counter = 0
    
    c = input("Type some text: ")
    if len(c) <= 0:
        print("Invalid input")
        return False

    for char in c:
        if char in check:
            counter += 1

    print(counter)
    
    
main()