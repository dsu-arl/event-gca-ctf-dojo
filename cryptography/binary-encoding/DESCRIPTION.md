## Challenge Description
In this challenge, you will learn about Binary Encoding!
Binary encoding is how computers store and process data at the lowest level—using only 0s and 1s. Each character in text is stored in memory as a byte (8 bits), which represents the ASCII value of the character in binary.

### How It Works:
Each character has an ASCII decimal value, and that value is then converted to an 8-bit binary number.

For example, the ASCII value of A is 65, which becomes 01000001 in binary.

Binary Table for uppercase letters:
```
Char: A        B        C        D        E        F        G        H        I
Dec : 65       66       67       68       69       70       71       72       73
Bin : 01000001 01000010 01000011 01000100 01000101 01000110 01000111 01001000 01001001

Char: J        K        L        M        N        O        P        Q        R
Dec : 74       75       76       77       78       79       80       81       82
Bin : 01001010 01001011 01001100 01001101 01001110 01001111 01010000 01010001 01010010

Char: S        T        U        V        W        X        Y        Z
Dec : 83       84       85       86       87       88       89       90
Bin : 01010011 01010100 01010101 01010110 01010111 01011000 01011001 01011010

```

For example, to encode the word HELLO:

- H → ASCII 72 → Binary 01001000
- E → ASCII 69 → Binary 01000101
- L → ASCII 76 → Binary 01001100
- L → ASCII 76 → Binary 01001100
- O → ASCII 79 → Binary 01001111

So, "HELLO" in binary is: `01001000 01000101 01001100 01001100 01001111`

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions given in `verify` to encode a secret word in binary and get the flag!
