
from morse import *
# Tesing
z=text_to_morse('Hi This is a test 123')
print(z)
play_morse_sound(z)
y=morse_to_text(z)
print(y)
play_text_sound(y)