
def passwordcheck(takeInput):
    specialChar = ['$', '@', '!', '&']
    val =True

    if len(takeInput) < 6:
        print("Length should be more than 6")
        val = False

    if len(takeInput) > 13:
        print("Length should not be more than 13")
        val = False

    if not any(char.isupper() for char in takeInput):
        print("Should have a Capital Char")
        val = False
    if not any(char.islower() for char in takeInput):
        print("Should have a sample char")
        val = False
    if not any(char.isdigit() for char in takeInput):
        print("should have a digit")
        val = False
    if not any(char in specialChar for char in takeInput):
        print("Should have a special char")
        val = False
    if val:
        return val


def main():
    takeInput = input("Enter your password:-")

    if (passwordcheck(takeInput)):
        print("valid password")
    else:
        print("invalid password")


if __name__ == '__main__':
    main()
