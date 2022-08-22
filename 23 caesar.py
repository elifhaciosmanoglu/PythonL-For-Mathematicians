def encrypt(text,k):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + k-65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result
#check the above function
text = "PYTHONFORMATHEMATICIAN"
k = 4   #shift time
print ("Text  : " + text)
print ("Shift : " + str(k))
print ("Cipher: " + encrypt(text,k))
