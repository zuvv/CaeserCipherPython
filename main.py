# ceaser cipher example
# Ted Pro
myMsg = 'get this message to the main server'
myShift = 13

def encrypt(text,shift):
    '''
    INPUT: text as a string and an integer for the shift value.
    OUTPUT: The shifted text after being run through the Caeser cipher.
    '''
    
    # Create a normal plain alphabet
    import string
    alphabet = string.ascii_lowercase 
    #array of integer character locations
    encrypt=list(range(len(text)))
    # Create a shifted version of this alphabet 
    # (Try slicing using the shift and then reconcatenating the two parts)
    
    firstpart = alphabet[:shift]
    secondpart = alphabet[shift:]
    #shifting is secondpart + firstpart to modify the alphabet
    shifted=secondpart+firstpart
    s = ""
    #print(shifted)
    #print(encrypt)
    # Use a for loop to go through each character in the original message.
    for i, letter in enumerate(text.lower()):
      if letter in alphabet:
        original_index=alphabet.index(letter)
        new_letter=shifted[original_index]
        encrypt[i]=new_letter
      else:
        ##array is filled with numbers, and needs to be replaced with spaces when there is a space otherwise it will keep a number at that location and will not be able to use the join function
        encrypt[i]=" "
    return(s.join(encrypt))






# ## Decryption
# Takes in the text, and the known shifted value.
def decrypt(text,shift):
    '''
    INPUT: A shifted message and the integer shift value
    OUTPUT: The plain text original message.
    '''
    
    # Create a normal plain alphabet
    import string
    alphabet = string.ascii_lowercase 
    decrypt=list(range(len(text)))
    f = ""
  
    # Create a shifted version of this alphabet with the shift value.
    firsthalf=alphabet[:shift]
    secondhalf=alphabet[shift:]
    shifted=firsthalf+secondhalf
    
    # Use a for loop to go through each character in the encrypted message.
    for i,letter in enumerate(text):
        if letter in alphabet:
    # Then figure out its index match in the plain alphabet and replace.
            original_index=alphabet.index(letter)
            new_letter=shifted[original_index]
            decrypt[i]=new_letter
        else:
            decrypt[i]=" "
    return(f.join(decrypt))

print("Message before encryption: ")
print(myMsg)
print('Encrypted Text:')
print(encrypt(myMsg,myShift))
print('Decrypted Text:')
print(decrypt(myMsg,myShift))