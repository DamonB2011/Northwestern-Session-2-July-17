shiftAmount = 3

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def encryptOrDecrypt(message, shouldEncrypt):
    charIndices = []
    # gets the index of each letter in the message
    for letter in message:
        if letter == " ":  # if it's a space, say -1
            charIndices.append(-1)
            continue
        charIndex = alphabet.index(letter.lower())
        charIndices.append(charIndex)

    # shifts the index over by the shift amount and adds it to a new string
    encryptedMessage = ""
    for index in charIndices:
        if index == -1:  # if it's a space
            encryptedMessage += " "
            continue
        # add the shift if encrypting, subtract it if decrypting
        if shouldEncrypt:
            index += shiftAmount
        if not shouldEncrypt:
            index -= shiftAmount
        index = index % len(alphabet)  # make sure to roll over (e.g. 28 becomes 2)
        encryptedMessage += str(alphabet[index])

    return encryptedMessage


def main():
    message = input("Please input your message: ")
    encryptedMessage = encryptOrDecrypt(message, True)
    print("\nEncrypted message: " + encryptedMessage)
    print("\nDecrypted message: " + encryptOrDecrypt(encryptedMessage, False))


main()
