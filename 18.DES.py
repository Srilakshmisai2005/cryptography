def generate_subkeys(initial_key):
    left_key = initial_key >> 28
    right_key = initial_key & 0xFFFFFFF

    subkeys = []

    for i in range(16):
        # Shift the halves based on shift schedule
        shifts = 1 if i in [0, 1, 8, 15] else 2
        left_key = ((left_key << shifts) & 0xFFFFFFF) | (left_key >> (28 - shifts))
        right_key = ((right_key << shifts) & 0xFFFFFFF) | (right_key >> (28 - shifts))

        # Combine the two halves to form the subkey
        combined_key = (left_key << 28) | right_key
        subkey = (combined_key >> 36) & 0xFFFFFF
        subkeys.append(subkey)

    return subkeys

def main():
    initial_key = 0x0123456789ABCDEF  # 64-bit key

    subkeys = generate_subkeys(initial_key)

    print("Generated subkeys:")
    for i, subkey in enumerate(subkeys):
        print(f"Round {i + 1}: {subkey:06X}")

if __name__ == "__main__":
    main()
