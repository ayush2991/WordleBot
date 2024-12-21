INITIALIZE_MESSAGE = "Starting WordleBot..."

class WordleBot:
    def __init__(self):
        pass

    def dictionary(self):
        return ["apple", "spade", "clown", "guilt", "grave"]

def main():
    print(INITIALIZE_MESSAGE)
    wordleBot = WordleBot()

if __name__ == "__main__":
    main()