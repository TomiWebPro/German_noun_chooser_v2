import json

def extract_data(line):
    parts = line.strip().split(' ')
    if len(parts) >= 2:
        gender = parts[0] if parts[0] in ['der', 'die', 'das'] else None
        german_word = parts[1] if gender else parts[0]

        english_translation = ''
        if '(' in line:
            translation_start = line.find('(') + 1
            translation_end = line.find(')', translation_start)
            english_translation = line[translation_start:translation_end].strip()

        return {"gender": gender, "german": german_word, "english": english_translation}
    else:
        return None

def main():
    all_word_data = []

    print("Enter word data in the format: gender/None word (translation)")
    print("Type 'done' on a new line when you're finished.")

    while True:
        line = input("> ")
        if line.lower() == 'done':
            break
        data = extract_data(line)
        if data:
            all_word_data.append(data)

    with open('output.json', 'w', encoding='utf-8') as file:
        json.dump(all_word_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
