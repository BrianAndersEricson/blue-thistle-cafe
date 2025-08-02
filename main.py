from blessed import Terminal
from ollama import ChatResponse, chat


def render_logo(width, path="assets/ascii/logo.txt"):
    with open(path, "r") as f:
        for line in f:
            print(line.strip("\n").center(width))


def main():
    term = Terminal()

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        # Clear the screen
        print("\033[2J\033[3J\033[H")

        render_logo(term.width)

        loop = True
        while loop:
            
            key = term.inkey()
            
            if key.lower() == "q":
                loop = False


if __name__ == "__main__":
    main()
