def main():
    #write your code below this line
    age = int(input("How old are you?"))
    if (age < 0 or age > 120):
      print("Impossible!")
    else:
      print("OK")

if __name__ == '__main__':
    main()
