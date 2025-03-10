from textnode import *


def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy.__repr__())
    return

if __name__ == "__main__":
    main()