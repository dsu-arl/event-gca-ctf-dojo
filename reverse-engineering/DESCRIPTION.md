## Welcome to the Reverse Engineering Module

This module will introduce different topics under the reverse engineering umbrella. Reverse engineering can be extremely complex involving many moving parts, or it can be as easy as parsing output from a tool! The variety of topics covered by reverse engineering makes it a dynamic and fun sandbox environment.

This module will frequently use the term "binary" to refer to a program that a user or operating system would run. Examples of binaries (programs) include: Chrome, Firefox, calculator, Fortnite, Microsoft Word, Valorant, League of Legends, Dropbox. The list can go on forever! Nearly anything you interact with on a computer is a program. 

The purpose of reverse engineering is to understand the internal workings of these binaries, and what makes them work. Most often this is done to find vulnerabilities in binaries, but reverse engineering can also be used to troubleshoot problems, or bugs, with binaries and develop solutions.

### Analysis Techniques

Broadly, reverse engineering can be divided into two topics: static and dynamic analysis. The purpose of static analysis is to inspect the binary without executing it. This can be important when analyzing malicious software (malware) because you don't want to accidently infect your computer! Tools under this category include: objdump, strings, IDA, Ghidra. Dynamic analysis is the opposite; inspecting how the binary works while it is running (executing.) Tools under this category include debuggers like GDB and WinDBG. Both techniques have pros and cons, and employing both while inspecting a binary is very common. These will be discussed more as needed within the challenges.