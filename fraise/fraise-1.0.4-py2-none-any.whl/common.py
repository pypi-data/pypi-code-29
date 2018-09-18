import words

def generate(word_count = 4):
    word_list = []
    for _ in range(word_count):
        word_list.append(words.get_random_word())
    passphrase = ' '.join(map(str, word_list))
    return(passphrase)

if __name__ == "__main__":
    print(generate())
