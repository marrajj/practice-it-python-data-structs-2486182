from collections import deque
def check_palindrome(word):
    d = deque(word)
    print(d.popleft())

def main():
    word = "taco"
    print(check_palindrome(word))
    return

if __name__ == "__main__":
    main()