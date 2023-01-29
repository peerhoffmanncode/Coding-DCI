
def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
     return bits.replace('111111', '-').replace('11', '.').replace('0000', ' ').replace('0', '')

def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message

    word = ""
    for k in morse_code.replace("  "," ").split(" "):
        if k == "":
            word = word + " "
        elif k in MORSE_CODE:
            word = word + MORSE_CODE[k]
            
    return word

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

test = decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')

#'1100 1100 1100 1100 0000 1100 0000 1111 1100 1100 1111 1100 1111 1100 00000000000011001111110011111100111111000000110011001111110000001111110011001100000011')

print(".... . -.--   .--- ..- -.. .")
print((decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))

print(decode_morse(test), 'HEY JUDE')