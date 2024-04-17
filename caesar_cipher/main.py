import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, direction_value):
    i = 0
    j = 0
    plain_text = list(plain_text)
    if direction_value == "decode":
        shift_amount *= -1
    while i < len(plain_text):
        if plain_text[i].isalpha():
            j = alphabet.index(plain_text[i])
            j = j + shift_amount
            plain_text[i] = alphabet[j]
            i = i + 1
        else:
            plain_text[i] = plain_text[i]
            i = i + 1
            
    plain_text = "".join(plain_text)
    print(f"Here is the {direction_value}d result: {plain_text}")

print(art.logo)

restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, direction_value = direction)
    restart = input("Type 'yes' if you want to go again. Otherwise typr 'no'.\n")
