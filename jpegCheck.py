import sys

def checkFile():
    if len(sys.argv) < 2:
        print("File must be specified")
        return

    try:
        rp = open(sys.argv[1], 'rb')
    except FileNotFoundError:
        print("File not found")
        return

    if rp == None:
        print("File not readable")
        return
    if rp.read(3) == b'\xff\xd8\xff':
        print("Yes this is an image file")
    else:
        print("Not an image file")

if __name__ == "__main__":
    checkFile()
