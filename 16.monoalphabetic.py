def letter_frequency_attack(ciphertext, top_n):
    english_letter_freq = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09,
        'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23,
        'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
        'Q': 0.10, 'Z': 0.07
    }

    letter_freq = {}
    for letter in ciphertext:
        if letter.isalpha():
            letter = letter.upper()
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)
    possible_plaintexts = []

    for i in range(min(top_n, len(sorted_freq))):
        cipher_letter = sorted_freq[i][0]
        freq_diff = {}
        for english_letter, english_freq in english_letter_freq.items():
            diff = abs(english_freq - (letter_freq[cipher_letter] / len(ciphertext) * 100))
            freq_diff[english_letter] = diff

        sorted_diff = sorted(freq_diff.items(), key=lambda x: x[1])
        possible_plaintext = ''
        for letter in ciphertext:
            if letter.isalpha():
                letter = letter.upper()
                if letter == cipher_letter:
                    possible_plaintext += sorted_diff[0][0]
                else:
                    possible_plaintext += letter
            else:
                possible_plaintext += letter

        possible_plaintexts.append(possible_plaintext)

    return possible_plaintexts


# Example usage
ciphertext = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
top_n = 10
plaintexts = letter_frequency_attack(ciphertext, top_n)

for i, plaintext in enumerate(plaintexts):
    print(f"Plaintext {i+1}: {plaintext}")
