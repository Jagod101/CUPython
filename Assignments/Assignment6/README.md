# Assignment 6 - Functions
```
Zach Jagoda
Student ID: 2274813
Student Email: jagod101@mail.chapman.edu
CPSC230
Assignment 6 - Functions
```
```
Source Files: complement.py, latin.py, README.md
Errors: N/A
References: N/A
```
Program Descriptions:
```
Complement.py
Write a module, complement.py, with a function, complement, that returns the complement of a DNA string. Also provide a function, rev_complement that takes a
DNA sequence as string input and returns the reverse complement of the sequence as a string. Recall that the valid alphabet is {A, C, T, G} and that A-T and G-C are complements. A reverse complement is found by reversing the input string and replacing every nucleotide with its complement. This means that your rev_complementfunction should use your complement function internally rather than duplicating code.Your functions should do appropriate error checking and return an error message asappropriate. Test your functions with input from the user.
For example, if your input is ACTG, your complement should be TGAC and your reverse complement should be CAGT.
```
```
Latin.py
Write a module, latin.py, with two functions word_to_pig and name_to_pig. Your word_to_pig function will take 1 parameter that converts the word based on the belowrules. Your name_to_pig function takes 2 input parameters, first_name and last_name, and will use your word_to_pig function to do the translation to avoid duplicating code. Your name_to_pig function returns the names in pig Latin. Test your functions with input from the user, you only need test a name, not a word and then a name.

Please use the following guidelines for Pig Latin:
● Words beginning with consonants: move the consonant from the start of the word to the end of the word. Then add the suffix "ay" to the end of the word. For
example, the word "hello" would become ellohay, the word "duck" would become uckday.
● Words beginning with vowels: all you need to do is add "yay" to the end of the word. You don't need to change any letters around, just say the word as normal then add "yay" to the end. For example: the word "egg" becomes eggyay and the word "ultimate" becomes ultimateyay.
```
