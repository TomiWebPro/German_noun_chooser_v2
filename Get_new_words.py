import json
import random


def load_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def save_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def save_txt_file(filename, words_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for word_data in words_list:
            gender = word_data["gender"]
            german_word = word_data["german"]
            english_translation = word_data["english"]

            line = ""
            if gender:
                line += f"{gender} "
            line += german_word

            if english_translation:
                line += f" ({english_translation})"

            file.write(line + '\n')


def main():
    german_words = load_json_file('german_words_json.json')
    learnt_words = load_json_file('learnt_words.json')

    if not german_words:
        print("No input files found.")
        return

    learnt_word_set = set(word_data["german"].lower()
                          for word_data in learnt_words)

    print("Enter the number of new words to learn:")
    num_new_words = int(input("> "))

    if num_new_words <= 0:
        print("Number of new words must be greater than 0.")
        return

    potential_new_words = [
        word_data for word_data in german_words if word_data["german"].lower() not in learnt_word_set]

    if len(potential_new_words) < num_new_words:
        print("Not enough unique words available for learning.")
        return

    # Shuffle the list of potential new words
    random.shuffle(potential_new_words)

    new_words = potential_new_words[:num_new_words]

    new_words_json_filename = 'new_words.json'
    new_words_txt_filename = 'new_words.txt'

    save_json_file(new_words_json_filename, new_words)
    save_txt_file(new_words_txt_filename, new_words)

    print(f"{num_new_words} new words saved to {new_words_json_filename} and {new_words_txt_filename}.")


if __name__ == "__main__":
    main()
