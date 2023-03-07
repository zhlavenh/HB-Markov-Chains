"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_contents = open(file_path)

    file_content_string = " ".join(file_contents.read().splitlines())

    file_contents.close()


    return file_content_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    #make a set of keys from string so there are no duplicate pairs
    key_from_string = set()

    text_string = text_string.split(" ")

    word1 = 0
    word2 = 1
    word3 = 2

    while word3 <= (len(text_string)-1):
        key = (text_string[word1], text_string[word2])
        value = [text_string[word3]]

        chains[key]=value

        if key not in chains.keys():
            chains[key] = value
        
        elif key in chains.keys():
            chains.get(key, chains[key] + value) 


        word1 += 1
        word2 += 1
        word3 += 1

    print(chains)

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)

# print(open_and_read_file("green-eggs.txt"))