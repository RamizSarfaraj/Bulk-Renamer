import os


def main():
    """
    This function helps rename a bulk of files at once.
    """
    try:
        i = int(input("Enter the starting point : ")) 
        # path of the folder
        path = str(input("Enter the path of the folder : "))
        # The name you want to give to those files.
        # rename = str(input("Enter the new name you want to give : "))
        rename = str(input("Enter the first name : "))
        path = path + "/"
        # file extension
        extension = str(input("Enter the extension : (empty if nothing) : "))
        for filename in os.listdir(path):
            my_dest = rename + str(i) + extension
            my_source = path + filename
            my_dest = path + my_dest
            os.rename(my_source, my_dest)
            i += 1
    except:
        print("\nOops! Something is wrong.")
        print("\nPlease look for the following possible errors : \n 1. Check if '/' is present at the end of the folder path. \n 2. May the extension doesn't exist.\n\n")
if __name__ == '__main__':
    main()
