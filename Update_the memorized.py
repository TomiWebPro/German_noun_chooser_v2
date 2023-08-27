import json


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
    with open(filename, 'a', encoding='utf-8') as file:
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


def mark_as_learned(learnt_words, new_words_filename):
    new_learned_words = []
    with open(new_words_filename, 'r', encoding='utf-8') as file:
        new_words_lines = file.readlines()

    for line in new_words_lines:
        parts = line.strip().split(' ')
        if parts:
            german_word = parts[0].strip('()')
            if any(german_word == w["german"].lower() for w in learnt_words):
                continue

            new_learned_words.append({"gender": parts[0] if parts[0] in ['der', 'die', 'das'] else None,
                                      "german": parts[1] if parts[0] in ['der', 'die', 'das'] else parts[0],
                                      "english": ' '.join(parts[2:]).strip('()') if '(' in line else parts[-1]})

    if new_learned_words:
        learnt_words.extend(new_learned_words)
        save_json_file('learned_words.json', learnt_words)
        save_txt_file('learned_words.txt', new_learned_words)

        # Add an empty line at the end of the txt file
        with open('learned_words.txt', 'a', encoding='utf-8') as file:
            file.write('\n')

        print(f"Words marked as learned and saved to learned_words.json and learned_words.txt.")
    else:
        print("No new words to mark as learned.")


def main():
    learnt_words = load_json_file('learned_words.json')
    new_words_filename = 'new_words.txt'

    print("Have you memorized the words in new_words.txt? (yes/no):")
    answer = input("> ").strip().lower()

    if answer == 'yes':
        mark_as_learned(learnt_words, new_words_filename)
    elif answer == 'no':
        print("No action taken.")
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
