## Challenge Description
In this challenge, you will decode a word using binary ASCII encoding!

### How It Works:
Binary ASCII Table:
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

For example, to decode the binary values: `01010111 01001111 01010010 01001100 01000100`
we find the binary in the table and replace them with the correct character:

- 01010111 → W
- 01001111 → O
- 01010010 → R
- 01001100 → L
- 01000100 → D

So, the decoded message is: WORLD

### Challenge Steps
1. Start the challenge
2. Run `verify`
3. Follow the instructions to decode a secret binary message and get the flag!
