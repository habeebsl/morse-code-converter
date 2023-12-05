morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '"': '.-..-.', '@': '.--.-.',
    
    ' ': ' '
}

#collect inputs from the user
to_english = input("would you like to convert to english ")
user_input=input()


converted = []

#if input(to_english) is no then convert to morse code
if to_english == 'no':
 for i in range(len(user_input)):
    if user_input[i].upper() in morse_code_dict:
        converted.append(morse_code_dict[user_input[i].upper()])
    else:
        print("Not Found")
        break

 print("".join(converted))


#if input(to_english) is yes then convert to morse code
else:
 separated_morse=user_input.split(" ")
 for i in range(len(separated_morse)):
  for key, value in morse_code_dict.items():
     if separated_morse[i] == value:
        converted.append(key)
     else:
        continue
 print("".join(converted))