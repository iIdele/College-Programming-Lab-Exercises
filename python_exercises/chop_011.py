import sys

def chop(s):
    return s[1:len(s) - 1]

def main():
    for line in sys.stdin:
        new = chop(line.strip())
        if new:
            print(new)

if __name__ == '__main__':
    main()