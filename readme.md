Python script to decrypt a message.

Messages are in the format:

number string
number string
number string
...

Decrypting the message works by building the numbers into a pyramid, and using the word from the end of each line:

1
2 3
4 5 6
7 8 9 10

In this case the decrypted messaged would be strings related to numbers 1, 3, 6, 10.
