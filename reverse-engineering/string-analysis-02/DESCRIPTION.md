## Challenge Description
This challenge uses the `strings` command again. This time however there are multiple passwords that you must find and enter in the correct order.

## How It Works
`strings` is often just the first step in understanding the inner workings of a binary. `strings` provides a quick and simple way to view what the program is attempting to do by analyzing its strings.

This challenges gives you the chance to find secret plain-text passwords and guess the order they're used in. Once you guess the correct order, you'll receive the final password to enter into the verify script!

## Challenge Steps
Locate the unusual strings within the challenge binary `locateTheStrings`. The string will be human readable, but it will also contain special characters to make it stand out a bit more. If using the GUI Desktop Workspace option, you will need to navigate to the "challenge" folder with the command: `cd /challenge`

If an incorrect string is entered on the command line, there is a possibility the program will pause, or "hang." If this is the case press and hold the "CTRL" button and then press the "C" button. This will terminate the program and you will be able to run it again.

1. Run `strings` against the challenge binary.
2. Examine the output and locate the passwords.
3. Enter the passwords in the correct order to get the final password.
3. Run the `verify` script and when prompted enter the challenge string.