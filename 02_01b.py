from collections import deque
def main():
    foods = deque(maxlen=5)
    foods.append("STA1")
    print(foods)
    return

if __name__ == "__main__":
    main()