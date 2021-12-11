


def compress_str(input:str) -> str:

    if not input.isalpha():
        raise ValueError("El texto de entrada solo debe contener letras de la a-z o de la A-Z.")

    letters_counter = {}
    for letter in input:
        if letter in letters_counter.keys():
            letters_counter[letter] += 1
        else:
            letters_counter[letter] = 1

    compressed_list = [key + str(count) for key, count in letters_counter.items()]
    compressed_str = "".join(compressed_list)
    return compressed_str