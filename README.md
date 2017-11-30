anagram
==========================================

## What is the runtime complexity?

Variables:
- N: length of dictionary
- W: length of the word

Worst Case Offline: `O(NWlog(W)+N^2log(N))`
- the first loop `O(N)`
  - sorting the word `O(Wlog(W))`
- the second loop `O(N)`
  - sorting the values in the dict entry `O(Nlog(N))`

Worst Case Online: `O(Wlog(W)+N)`
- sort on input word
  - `O(Wlog(W))` sort
- access to dictionary `dict_words`
  - `O(N)` in amortized worst case

## What is the memory complexity?
Variables:
- N: length of dictionary
- W: length of the word

`O(N)`
- create `dict_words`

## Algorithm design

The offline step `preprocess()` adds all the words to a dictionary `dict_words` using an `index` that is the original `word`'s letters sorted in alphabetical order. This means that `beta` and `bate` will share the same index and will thus be located at the same `index` in `dict_words`. There is a final step to sort the words in the `dict_words` before concatenating all the anagrams and storing them again into `dict_words`.

The online step `anagram_finder()` will recreate the `word`'s `index`, using the same strategy as above, into the `dict_words` and print `dict_words[index]`.
