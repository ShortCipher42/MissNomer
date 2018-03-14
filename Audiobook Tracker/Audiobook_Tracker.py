import nibbler, os

def main():

    

if __name__ == '__main__':
    filename = '%APPDATA%/Tracker/library.db'
    if(os.path.exists(filename)):
        pass
    else:
        nibbler.creator(filename)
    main()

