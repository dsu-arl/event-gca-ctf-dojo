## Challenge Description
This challenge will require you to _decrypt_ a word! 
Imagine if you were an enemy soldier and intercepted a secret message from Julius Caesar - you must learn how to decrypt it!

### How It Works:

**Shift Value:** Just like with encrypting, the shift value determines how many places each letter has been moved.
This time, to decrypt a message, instead of _adding_, we need to _subtract_ the shift amount. 
For example, with a shift of 3:

- D (4) becomes A (1)
- E (5) becomes B (2)
- A (1) wraps around and becomes X (24)

```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
```

**Decryption:** To decrypt the message, shift the letters back.

## Challenge Steps
1. Start the challenge
2. Run `solve`
3. Follow the instructions given in `solve` to decrypt a secret word and get the flag!
