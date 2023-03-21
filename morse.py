from playsound import playsound
import pyttsx3 as pyttsx
import time

MORSE_CODE_TABLE = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

inv_MORSE_CODE_TABLE = {v: k for k, v in MORSE_CODE_TABLE.items()}

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    result = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in inv_MORSE_CODE_TABLE:
                result += inv_MORSE_CODE_TABLE[letter]
        result += ' '
    return result

def text_to_morse(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += MORSE_CODE_TABLE[letter.upper()] + ' '
        else:
            cipher += ' '
 
    return cipher

def play_morse_sound(morse):
    for m in morse:
        if m=='.':
            playsound('dit.wav')
        elif m=='-':
            playsound('dah.wav')
        else:
            time.sleep(0.5)
def play_text_sound(text):
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()