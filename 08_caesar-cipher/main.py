

def encode(word_: str, shift_: int) -> str:
    word_ = word_.lower()
    res = ""
    for ch in word_:
        if ord('a') <= ord(ch) <= ord('z'):
            res += chr((ord(ch) - ord('a') + shift_) % 26 + ord('a'))
        else:
            res += ch
    return res


while True:
    ans = input("Do you want to (E)ncode a message or (D)ecode one? ").lower()[0]
    word = input("Input the text: ").lower()
    shift = int(input("What number is your key to shift by? "))
    if ans == 'd':
        shift = -shift

    print(encode(word, shift))
    if input("Do you want to go again? (y/n) ").lower()[0] != 'y':
        break
