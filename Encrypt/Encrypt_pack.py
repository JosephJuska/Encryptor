from random import choice
from string import ascii_uppercase
from string import ascii_letters

l = ['\n','\t'] + list(chr(i) for i in range(32,127))
#95
d1 = {y:x for x,y in enumerate(l)}
d2 = {x:y for x,y in enumerate(l)}

d1_uppercase = {y:x for x,y in enumerate(ascii_uppercase)}
d2_uppercase = {x:y for x,y in enumerate(ascii_uppercase)}

d1_letters = {y:x for x,y in enumerate(sorted(ascii_letters))}
d2_letters = {x:y for x,y in enumerate(sorted(ascii_letters))}

def test(text: str) -> str:
    for i in text:
        if i not in d2.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption')

def test_uppercase(text: str) -> str:
    for i in text:
        if i not in d2_uppercase.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption upper_case')
        
def test_letters(text: str) -> str:
    for i in text:
        if i not in d2_letters.values():
            raise ValueError(f'Text value |{i}| does not match the base for encryption letters_only')

def test_key(text: str) -> str:
    for i in text:
        if i not in d2.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption')

def test_uppercase_key(text: str) -> str:
    for i in text:
        if i not in d2_uppercase.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption upper_case')
        
def test_letters_key(text: str) -> str:
    for i in text:
        if i not in d2_letters.values():
            raise ValueError(f'Key value |{i}| does not match the base for encryption letters_only')

def rotation(rotation_number: int,text: str) -> str:
    '''
    Function to encrypt text with rotation number.
    '''
    new_text = ''
    for i in text:
        n = d1[i]
        n += rotation_number
        if n > 96:
            n %= 97
        
        new_text += d2[n]
    
    return new_text

def key_encrypt(key: str,text: str) -> str:
    '''
    Function to encrypt text with a key.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            j = 0

        n = d1[i]
        m = d1[key[j]]
        n += m
        if n > 96:
            n %= 97
        
        new_text += d2[n]
        j += 1
    
    return new_text

def rotation_and_key(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to encrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1[i]
            n += rotation_number
            if n > 96:
                n %= 97
            
            new_text += d2[n]
            continue

        n = d1[i]
        m = d1[key[j]]
        n += m
        if n > 96:
            n %= 97
        
        new_text += d2[n]
        j += 1
    return new_text

def key_random(key: str,text: str) -> str:
    '''
    Function to encrypt text with key.
    If key is not long enough,random values will be used.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1[i]
            m = d1[choice(d2)]
            n += m
            if n > 96:
                n %= 97
            
            new_text += d2[n]
            continue

        n = d1[i]
        m = d1[key[j]]
        n += m
        if n > 96:
            n %= 97
        
        new_text += d2[n]
        j += 1
    
    return new_text

def rotation_uppercase(rotation_number: int,text: str) -> str:
    '''
    Function to encrypt text with rotation number.
    Encryption is done by uppercase letters.
    '''
    new_text = ''
    for i in text:
        n = d1_uppercase[i]
        n += rotation_number
        if n > 25:
            n %= 26
        
        new_text += d2_uppercase[n]
    
    return new_text

def key_encrypt_uppercase(key: str,text: str) -> str:
    '''
    Function to encrypt text with a key.
    Encryption is done by uppercase letters.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            j = 0

        n = d1_uppercase[i]
        m = d1_uppercase[key[j]]
        n += m
        if n > 25:
            n %= 26
        
        new_text += d2_uppercase[n]
        j += 1
    
    return new_text

def rotation_and_key_uppercase(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to encrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    Encryption is done by uppercase letters.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1_uppercase[i]
            n += rotation_number
            if n > 25:
                n %= 26
            
            new_text += d2_uppercase[n]
            continue

        n = d1_uppercase[i]
        m = d1_uppercase[key[j]]
        n += m
        if n > 25:
            n %= 26
        
        new_text += d2_uppercase[n]
        j += 1
    return new_text

def key_random_uppercase(key: str,text: str) -> str:
    '''
    Function to encrypt text with key.
    If key is not long enough,random values will be used.
    Encryption is done by uppercase letters.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1_uppercase[i]
            m = d1_uppercase[choice(d2)]
            n += m
            if n > 25:
                n %= 26
            
            new_text += d2_uppercase[n]
            continue

        n = d1_uppercase[i]
        m = d1_uppercase[key[j]]
        n += m
        if n > 25:
            n %= 26
        
        new_text += d2_uppercase[n]
        j += 1
    
    return new_text

def rotation_letters(rotation_number: int,text: str) -> str:
    '''
    Function to encrypt text with rotation number.
    Encryption is done only by letters.
    '''
    new_text = ''
    for i in text:
        n = d1_letters[i]
        n += rotation_number
        if n > 51:
            n %= 52
        
        new_text += d2_letters[n]
    
    return new_text

def key_encrypt_letters(key: str,text: str) -> str:
    '''
    Function to encrypt text with a key.
    Encryption is done only by letters.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            j = 0

        n = d1_letters[i]
        m = d1_letters[key[j]]
        n += m
        if n > 51:
            n %= 52
        
        new_text += d2_letters[n]
        j += 1
    
    return new_text

def rotation_and_key_letters(rotation_number: int,key: str,text: str) -> str:
    '''
    Function to encrypt text when rotation number and key both are included.
    If key is long enough,rotation will not be used.
    Encryption is done only by letters.
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1_letters[i]
            n += rotation_number
            if n > 51:
                n %= 52
            
            new_text += d2_letters[n]
            continue

        n = d1_letters[i]
        m = d1_letters[key[j]]
        n += m
        if n > 51:
            n %= 52
        
        new_text += d2_letters[n]
        j += 1
    return new_text

def key_random_letters(key: str,text: str) -> str:
    '''
    Function to encrypt text with key.
    If key is not long enough,random values will be used.
    Encryption is done only by letters
    '''
    new_text = ''
    j = 0
    for i in text:
        if j >= len(key):
            n = d1_letters[i]
            m = d1_letters[choice(d2)]
            n += m
            if n > 51:
                n %= 52
            
            new_text += d2_letters[n]
            continue

        n = d1_letters[i]
        m = d1_letters[key[j]]
        n += m
        if n > 51:
            n %= 52
        
        new_text += d2_letters[n]
        j += 1
    
    return new_text