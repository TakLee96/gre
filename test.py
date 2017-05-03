from os import path
from sys import stdout
from random import randint


words = list()


vocab_path = path.join(path.dirname(__file__), "vocab.csv")
with open(vocab_path, "r") as vocab_file:
    for line in vocab_file:
        if len(line) != 0:
            word = tuple(map(lambda w: w.strip(), line.split(",")))
            words.append(word)


if __name__ == '__main__':
    cmd = "n"
    helper_string = "(n)ext / (q)uit / (w)ord / (m)eaning / (s)entence"
    print helper_string
    while cmd != "q" and len(words) > 0:
        if cmd == "n":
            index = randint(0, len(words) - 1)
            word = words.pop(index)
            print "%s [%s.]" % (word[0], word[1])
        elif cmd == "w":
            print "%s [%s.]" % (word[0], word[1])
        elif cmd == "m":
            print word[2]
        elif cmd == "s":
            print word[3]
        else:
            print helper_string
        stdout.write(">>> ")
        cmd = raw_input()
