from os import system
from random import choice
from Encrypt_pack import rotation
from Encrypt_pack import key_encrypt
from Encrypt_pack import rotation_and_key
from Encrypt_pack import key_random
from Encrypt_pack import rotation_letters
from Encrypt_pack import key_encrypt_letters
from Encrypt_pack import rotation_and_key_letters
from Encrypt_pack import key_random_letters
from Encrypt_pack import rotation_uppercase
from Encrypt_pack import key_encrypt_uppercase
from Encrypt_pack import rotation_and_key_uppercase
from Encrypt_pack import key_random_uppercase
from Encrypt_pack import test
from Encrypt_pack import test_uppercase
from Encrypt_pack import test_letters
from Encrypt_pack import test_key
from Encrypt_pack import test_uppercase_key
from Encrypt_pack import test_letters_key
def main():
    try:
        from argparse import ArgumentParser
        
    except:
        system('pip3 install argparse')
        from argparse import ArgumentParser

    parse = ArgumentParser(description="Encrypts a text",prog="Encrypter",epilog='For more information about this tool read |README.txt|')

    parse.add_argument('-t','--text',help='Path of the text file.',type=str)
    parse.add_argument('-n','--number',help ='Rotation number.',type=int,default=None,nargs='?')
    parse.add_argument('-p','--path',help='Path where encrypted text will be written.',nargs = '?',default='encrypted_text.txt',type=str)
    parse.add_argument('-k','--key',help='Key for encryption.',nargs='?',default=None,type=str)
    parse.add_argument('-rk','--randomised_key',help='If key is not as big as text,it will be filled with random values.',const=True,nargs='?',default=False,type=bool)
    parse.add_argument('-uc','--upper_case',help='Text will be encrypted with the base of uppercase letters.',const=True,nargs='?',default=False,type=bool)
    parse.add_argument('-lo','--letters_only',help='Text will be encrypted with the base of only letters.',const=True,nargs='?',default=False,type=bool)
    
    args = parse.parse_args()

    try:
        if not args.number and not args.key:
            raise ValueError('One(key or rotation number) or both should be given')

        if args.upper_case and args.letters_only:
            raise ValueError('Only one(upper_case or letters_only) should be given')
        
        with open(args.text,'r+') as f:
            text = f.read().strip()

        if not args.upper_case and not args.letters_only:
            test(text)
            if args.number and not args.key:
                new_text = rotation(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully encrypted text to {args.path}')
        
            if not args.number and args.key:
                test_key(args.key)
                if not args.randomised_key:
                    new_text = key_encrypt(key=args.key,text=text)

                else:
                    new_text = key_random(key=args.key,text=text)

                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')

            if args.number and args.key:
                test_key(args.key)
                new_text = rotation_and_key(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')

        if args.upper_case and not args.letters_only:
            test_uppercase(text)
            if args.number and not args.key:
                new_text = rotation_uppercase(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully encrypted text to {args.path}')
        
            if not args.number and args.key:
                test_uppercase_key(args.key)
                if not args.randomised_key:
                    new_text = key_encrypt_uppercase(key=args.key,text=text)

                else:
                    new_text = key_random_uppercase(key=args.key,text=text)

                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')

            if args.number and args.key:
                test_uppercase_key(args.key)
                new_text = rotation_and_key_uppercase(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')
        
        if not args.upper_case and args.letters_only:
            test_letters(text)
            if args.number and not args.key:
                new_text = rotation_letters(rotation_number=args.number,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)

                    print(f'Successfully encrypted text to {args.path}')
        
            if not args.number and args.key:
                test_letters_key(args.key)
                if not args.randomised_key:
                    new_text = key_encrypt_letters(key=args.key,text=text)
                
                else:
                    new_text = key_random_letters(key=args.key,text=text)
                    
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')

            if args.number and args.key:
                test_letters_key(args.key)
                new_text = rotation_and_key_letters(rotation_number=args.number,key=args.key,text=text)
                with open(args.path,'w+') as nf:
                    nf.write(new_text)
                
                    print(f'Successfully encrypted text to {args.path}')
        

    except FileNotFoundError:
        print(f'Given path {args.path} or given text file {args.text} does not exist')
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()