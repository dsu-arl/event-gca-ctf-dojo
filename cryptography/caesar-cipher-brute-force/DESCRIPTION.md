## Challenge Description
If you manage to intercept a secret message, you likely won't be given the shift amount with it. 
In this challenge, you will try to break the encryption on some intercepted ciphertext! 

### How It Works:

**Brute Force**: Using brute force to find the shift amount (key) requires you to try decrypting your ciphertext with every possible key. 
From there, you can look at all of the resulting "plaintexts", and identify the original message. 
Most keys will result in gibberish - but one key will work! 

For these examples, we have 26 possible keys (since the Caesar Cipher wraps around), so brute force doesn't take too long.
But note that with other encryption algorithms, brute forcing can take _centuries_ to try all possible combinations.

**Frequency Analysis**: One way to help minimize the number of keys you need to try is to perform frequency analysis on the ciphertext. 
In the any language, there are several letters and combinations of letters that are used more frequently than others. 
For example, in English, the most commonly occuring letters and combinations are `E`, `T`, `A`, `O`, `TH`, `HE`, and `IN`.  
To utilize frequency analysis - find the most common letters in your ciphertext and try replacing them with the common letters above. 

Note that frequency analysis works best on long ciphertexts, with more letters that are repeated. 
There are also many encryption algorithms that are not vulnerable to this type of analysis. 
In this challenge specifically, frequency analysis will not be overly helpful - but you can always try it!

This challenge will give you only an encoded word. You will need to decrypt it without knowing the shift amount.
Try modifying your script from the previous challenge to try every possible key (1-26)!

## Challenge Steps
1. Start the challenge
2. Run `solve`
3. `solve` will give you the ciphertext
4. Write a script to brute force and decode your ciphertext
5. Run `solve` again and enter the plaintext your script found - and get the flag!
