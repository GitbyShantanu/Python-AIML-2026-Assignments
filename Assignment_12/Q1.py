# WAP which accepts one character and check whether it is vowel or consonant.

def chkCharacter(ch):
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    
    return False

def main():
    char = input("Enter a character: ")
    ans = chkCharacter(char)
    if ans:
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")

if __name__ == "__main__":
    main()