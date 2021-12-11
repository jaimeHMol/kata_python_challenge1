from compress import compress_str


def main():
    input_str = input("Ingrese el texto a 'comprimir': ")
    output_str = compress_str(input_str)
    print(f"Texto comprimido: {output_str}")

if __name__ == "__main__":
    main()