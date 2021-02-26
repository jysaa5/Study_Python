import re

special_chars_remover = re.compile("[^\w'|_]")


def main():
    sentence = "Bag-of-Words 모델을 Python으로 직접 구현하겠습니다."
    bow = create_BOW(sentence)

    print(bow)


def create_BOW(sentence):
    bow = {}
    sentence_lowered = sentence.lower()
    sentence_without_special_characters = remove_special_characters(sentence_lowered)
    splitted_sentence = sentence_without_special_characters.split()
    splitted_sentence_filtered = [
        token
        for token in splitted_sentence
        if len(token) >= 1
    ]

    print(sentence_without_special_characters)
    print(splitted_sentence_filtered)

    for token in splitted_sentence_filtered:
        bow.setdefault(token, 0)
        bow[token] += 1

    return bow


def remove_special_characters(sentence):
    return special_chars_remover.sub(' ', sentence)


if __name__ == "__main__":
    main()
