## Challenge Description
Manual encryption and decryption can be rather tedious. Unlike Julius Caesar, we have modern computers - let's write a script to do the work for us!

### How It Works:
This challenge will give you an encoded word and the amount it was shifted by during the encryption process. You will need to decrypt it. 
The secret word will be fairly long, so a script will come in handy!

You can use any programming or scripting language to make your own Caesar cipher solver. 
Here is the algorithm:

- Get the secret word (ciphertext)
- Get the shift amount
- For each character in the ciphertext:
    - Convert the character to a number
    - Subtract the original shift amount
        - Because a letter may need to wrap around, consider using mod (%)!
    - Either append or replace each letter you decode
- Print the resulting plaintext!

## Challenge Steps
1. Start the challenge
2. Run `solve`
3. `solve` will give you the ciphertext and the shift amount used to encrypt
4. Write a script to decode your ciphertext
5. Run `solve` again and enter the plaintext your script found - and get the flag!
