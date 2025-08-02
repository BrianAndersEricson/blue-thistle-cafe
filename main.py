from blessed import Terminal

def main():
    term = Terminal()

    with term.cbreak(), term.hidden_cursor():
        break

if __name__ == "__main__":
    main()
