# basic-hash-hiding
This project is a simple Python application that demonstrates the hiding property of cryptographic hash functions.

It takes a secret input (x) from the user, combines it with a randomly generated value (r), and hashes the result as H(r || x).
The goal is to ensure that the original secret cannot be guessed from the hash output.
The hashing is done using various algorithms provided by Python’s built-in hashlib module.
