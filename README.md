# Methods of Analysis of Textual Data

## Automata

- Implementation of a **DFA** to process a string with alphabet = {0,1}, to find out if it contains an even or odd number of 1's.
Usage : `python dfa.py 1000001`
- Implementation of a **NFA** to process a string with alfabet = {0,1}, to find out if it ends in 01.
Usage: `python nfa.py 1000001`

## Exact Pattern Matching

Search for specific words in a 50MB(for instance) file using different algorithms to measure their performance. Algorithms include:

1. **Brute Force** : `python brute_force.py Wolcott examples/english.50MB`
2. **DFA** : `python dfa.py Wolcott examples/english.50MB`
3. **Knuth-Morris-Pratt** : `python kmp.py Wolcott examples/english.50MB`
4. **Boyer-Moore** : `python boyer-moore.py Wolcott examples/english.50MB`

## Approximate Pattern Matching

Using an **NFA** to compare if two words are approximate the same. Usage: `python nfa.py cenas cenaaas 2`

## Text Document Preprocessing
Creating and information retrieval system. Both the Vector Model exercises were not implemented.
It include:

1. **Text Preprocessing**
2. **Inverted Index**
3. **Index Compression**
4. **Query System**

Usage: `python main.py reuters/reut2-000.sgm stock AND impact`

 
