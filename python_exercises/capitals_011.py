import sys

def capital(s):
    return s[0].upper() + s[1:len(s)-1] + s[len(s) - 1].upper()

def main():
    for line in sys.stdin:
        if 1 < len(line.strip()):
            new = capital(line.strip())
            if new:
                print(new)

if __name__ == '__main__':
    main()