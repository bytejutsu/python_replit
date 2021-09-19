logo = '''

                                        _       _               
   ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                         |_|                    

''' 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    
    output = ""

    for i,letter in enumerate(text):

      if letter in alphabet:

        old_index_in_alphabet = alphabet.index(letter)

        new_index_in_alphabet = (old_index_in_alphabet + shift) % len(alphabet)

        output += alphabet[new_index_in_alphabet]
      else:
        output += letter  

    cipher = ''.join(output)
    print(cipher)

def decrypt(text, shift):
  new_shift = len(alphabet) - shift % len(alphabet)
  encrypt(text = text, shift = new_shift) 

def caeser(text, shift, direction):

  if direction == "encode":
    encrypt(text = text, shift = shift)
  else:
    decrypt(text = text, shift = shift)

def main():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  print("output: ")

  caeser(text = text, shift = shift, direction = direction)

  repeat = input("do you want to repeat the process? yes/no: ").lower()

  if repeat in "yes":
    main()
  else:
    print("program ended")  

print(logo)
main()    
