## Challenge Description
In this challenge you will learn about the Caesar cipher!
The Caesar cipher is one of the simplest and most well-known encryption techniques. 
It is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. 
Named after Julius Caesar, who reportedly used it to communicate with his generals, the cipher is easy to understand and implement.

### How It Works:

**Shift Value:** The key to the Caesar cipher is the shift value, which determines how many places each letter is moved. 
For example, with a shift of 3:

- A (1) becomes D (4)
- B (2) becomes E (5)
- Z (26) wraps around and becomes C (3)

```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

**Encryption:** To encrypt a message, each letter is replaced by the letter that is a fixed number of positions away in the alphabet. 
For example, the word "HELLO" with a shift of 3 becomes "KHOOR".

**Decryption:** To decrypt the message, the process is reversed by shifting the letters back by the same number of positions.

It is important to note that while the Caesar cipher is easy to use, it is not secure by modern standards. It can be easily broken with techniques such as frequency analysis, where common letters and patterns in the ciphertext are analyzed to reveal the original message. As a result, the Caesar cipher is primarily of historical interest and is often used for educational purposes to introduce concepts of encryption and cryptography.

## Challenge Steps
1. Start the challenge
2. Run `solve`
3. Follow the instructions given in `solve` to encrypt a secret word and get the flag!
