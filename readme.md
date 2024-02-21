 # Python Text Analysis and CoNLL File Reader

 [![github](https://img.shields.io/badge/GitHub-purbancz-181717.svg?style=flat&logo=github)](https://github.com/purbancz)
[![x](https://img.shields.io/badge/Twitter-@purbancz-00aced.svg?style=flat&logo=x)](https://twitter.com/purbancz)
[![linkedin](https://img.shields.io/badge/LinkedIn-Piotr_Urbańczyk-00aced.svg?style=flat&logo=linkedin)](https://www.linkedin.com/in/piotr-urba%C5%84czyk-9943ab17a/)
[![website](https://img.shields.io/badge/Website-Piotr_Urbańczyk-5087B2.svg?style=flat&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGQ9Ik0gMTIgMi4wOTk2MDk0IEwgMSAxMiBMIDQgMTIgTCA0IDIxIEwgMTAgMjEgTCAxMCAxNCBMIDE0IDE0IEwgMTQgMjEgTCAyMCAyMSBMIDIwIDEyIEwgMjMgMTIgTCAxMiAyLjA5OTYwOTQgeiIgZmlsbD0iI2ZmZiI+PC9wYXRoPgo8L3N2Zz4=)](https://www.copernicuscenter.edu.pl/en/person/urbanczyk-piotr-2/)

This repository contains two separate Python scripts. The first script is used for text analysis, including token generation, n-gram generation, token counting, and frequency analysis. The second script is a class for reading CoNLL (Conference on Natural Language Learning) files, which is a common format for storing linguistic data and annotations.

## Ngram Counter

This script reads a text file, generates tokens (words) and n-grams (contiguous sequence of n items from a given sample of text), counts the frequency of each token or n-gram, and prints the top k most frequent tokens or n-grams. It also handles ties in frequency when printing the top k tokens or n-grams.

### Usage

You can use the `print_top_k_ex_aequo_most_frequent_tokens(filename, k)` function to print the top k most frequent tokens from a file, including ties. Similarly, you can use the `print_top_k_ex_aequo_most_frequent_n_grams(filename, n, k)` function to print the top k most frequent n-grams from a file, including ties.

## CoNLL File Reader

The `open_conll` class opens a CoNLL file and allows you to iterate over the tokens in the file. It is designed to be used with Python's `with` statement, which allows for clean resource management.

### Usage

You can use the `open_conll` class to read a CoNLL file as follows:

```python
with open_conll("filename.conll") as infile:
    for token in infile:
        print(token)
```

This will print all tokens in the CoNLL file.