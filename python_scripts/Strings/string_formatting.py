def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for i in range(number):
        decimal = i + 1
        octal = oct(i + 1)
        hexadecimal = hex(i + 1)
        binary = bin(i + 1)
        print(str(decimal).rjust(width), octal[2:].rjust(width), hexadecimal[2:].rjust(width).upper(), binary[2:].rjust(width), sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)