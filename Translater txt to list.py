def extract_data(line):
    parts = line.strip().split(' ')
    if len(parts) >= 2:
        gender = parts[0] if parts[0] in ['der', 'die', 'das'] else None
        german_word = parts[1] if gender else parts[0]
        if '(' in line:
            translation_start = line.find('(') + 1
            translation_end = line.find(')', translation_start)
            english_translation = line[translation_start:translation_end].strip()
        else:
            english_translation = parts[-1]
        return [gender, german_word, english_translation]
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

    with open('output_translated_txt.txt', 'w', encoding='utf-8') as file:
        for word in all_word_data:
            file.write(str(word) + '\n')

if __name__ == "__main__":
    main()
