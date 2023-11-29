import collections
import operator

def shift_text(text, shift):
    shifted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            shifted_text += shifted_char
        else:
            shifted_text += char
    return shifted_text

def letter_frequency(text):
    letter_count = collections.Counter()
    for char in text:
        if char.isalpha():
            letter_count[char.lower()] += 1
    return letter_count

def likely_shifts(ciphertext):
    freq_analysis = letter_frequency(ciphertext)
    sorted_freq = sorted(freq_analysis.items(), key=operator.itemgetter(1), reverse=True)
    
    english_letter_frequencies = "etaoinshrdlcumwfgypbvkjxqz"
    possible_shifts = []

    for i in range(26):
        shift = (ord(sorted_freq[0][0]) - ord(english_letter_frequencies[i])) % 26
        shifted_text = shift_text(ciphertext, shift)
        possible_shifts.append((shift, shifted_text))
    
    return possible_shifts

if __name__ == "__main__":
    ciphertext = "Vjg'u gzrtkekpi kvu jktpggp vjg vaq ejct yjcv. Jgcf vjg xgta cna fg vjg yjcv jktpggp vjg xgta cna."

    top_n = int(input("Enter the number of top possible plaintexts to display: "))
    
    possible_shifts = likely_shifts(ciphertext)

    print("\nTop Possible Plaintexts:")
    for i in range(top_n):
        print(f"Shift {possible_shifts[i][0]}: {possible_shifts[i][1]}")
