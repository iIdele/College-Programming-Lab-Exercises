import sys

d_pos = {'1': ['2', '5', '6'],'2': ['1', '3', '5', '6', '7'],
  '3': ['2', '4', '6', '7', '8'],
  '4': ['3', '7', '8'],
  '5': ['1', '2', '6', '9', '10'],
  '6': ['1', '2', '3', '5', '7','9', '10', '11'],
  '7': ['2', '3', '4', '6', '8', '10', '11', '12'],
  '8': ['3', '4', '7', '11', '12'],
  '9': ['5', '6', '10', '13', '14'],
  '10': ['5', '6', '7', '9', '11', '13', '14', '15'],
  '11': ['6', '7', '8', '10', '12', '14', '15', '16'],
  '12': ['7', '8', '11', '15', '16'],
  '13': ['9', '10', '14'],
  '14': ['9', '10', '11', '13', '15'],
  '15': ['10', '11', '12', '14', '16'],
  '16': ['11', '12', '15']}

def testing(d, word):
    board = word
    for word in d:
        if word in board:
            board.replace(word, '', 1)
        else:
            return False
    return True

def find_words(d, which_pos):
    for pos in which_pos[d[0]]:
        l1 = []
        l2 = []
        l3 = []
        l3.append(pos)
        l1.append(l3)
        for word in d[1:]:
            for bog in l1:
                for position in which_pos[word]:
                    if position in d_pos[bog[-1]] and position not in bog:
                        new_bog = bog[:]
                        new_bog.append(position)
                        l2.append(new_bog)
            l1, l2 = l2, []
        if len(l1) > 0:
            return True

def main():
    with open(sys.argv[1]) as f:
        words = [line.strip() for line in f.readlines()]

    with open(sys.argv[2]) as f:
        wlist = [d.strip() for d in f.readlines() if len(d.strip()) > 2 and len(d.strip()) < 17 ]
    for word in words:
        ds = [d  for d in wlist if testing(d, word)]
        which_pos = {}
        i = 1
        for w in word:
            if w in which_pos:
                which_pos[w].append(str(i))
            else:
                which_pos[w] = [str(i)]
            i += 1
        l4 = []
        for d in ds:
            if find_words(d, which_pos):
                l4.append(d)
        score = {
        1 : 0,
        2 : 1,
        3 : 1,
        4 : 1,
        5 : 2,
        6 : 3,
        7 : 5
        }
        points = 0
        for d in l4:
            if len(d) < 8:
                points += score[len(d)]
            else:
                points += 11
        print('Possible points: {}'.format(points))

if __name__ == '__main__':
    main()