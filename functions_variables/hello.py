def main():
    name = input("What's your name? ")
    hello(name)


def hello(name="Nameless"):
    print(f"Hello, {name}")


def square(n):
    return n**2


# hello()
# hello(name)
if __name__ == "__main__":
    main()
