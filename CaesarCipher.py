alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','r','t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','r','t','u','v','w','x','y','z']
direction = input("type 'encode' to encrypt , type 'decode' to decrypt:\n ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def ceasar(plain_text,shift_amount,direction):
    cipher_text =""
    for i in plain_text:
       position = alphabet.index(i)
       if direction == "encode":
          new_position = position+shift_amount
          new_i = alphabet[new_position]
          cipher_text+=new_i
         
       elif direction == "decode":
             new_position=position - shift_amount
             new_j= alphabet[new_position]
             cipher_text += new_j
       
    if direction == "encode":
        print(f"The encoded text is {cipher_text}")   
    elif direction=="decode":
     print(f"The decoded text is {cipher_text}")   
ceasar(plain_text=text, shift_amount=shift,direction=direction)