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

    text_string = text_string.split(" ")

    word1, word2, word3 = 0, 1, 2

    while word3 <= (len(text_string)-1):
        key = (text_string[word1], text_string[word2])
        value = [text_string[word3]]

        if key not in chains.keys():
            chains[key] = value
        
        else:  
            chains[key] += value

        word1 += 1
        word2 += 1
        word3 += 1
    
    return chains


def make_text(chains):
    """Return text from chains."""
    words = []

    #Generatign random keys from dictionary
    link_list = [key for key in chains.keys()]
    link = choice(link_list)
    words += link
  

    while True:
        try:
            #Taking new key from tuple to use for connection
            new_key = (link[1], choice(chains[link]))
            words.append(new_key[1])
            link = new_key

        except KeyError:
            return ' '.join(words)






input_path = 'green-eggs.txt'
# input_path = 'test_file.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# print(open_and_read_file("green-eggs.txt"))