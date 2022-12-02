# http://adventofcode.com/2016/day/5

import hashlib

def main(part):

    index = 0
    answer = ['?'] * 8

    while True:

        word = ("uqwqemis{}".format(index)).encode('utf-8')

        m = hashlib.md5()
        m.update(word)
        hash_result = m.hexdigest()

        if hash_result[0:5] == '00000':
            try:
                i = answer.index('?') if part == 1 else int(hash_result[5])
                if answer[i] == '?':
                    answer[i] = hash_result[5 if part == 1 else 6]
            except:
                pass

            if '?' not in answer:
                print(f"Part {part}:", "".join(answer))
                return

        index += 1

if __name__ == '__main__':
    main(1) # 1a3099aa
    main(2) # 694190cd