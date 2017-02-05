# -*- coding: utf-8 -*-
import sys


def print_usage():
    """Prints usage info."""
    print "Description: Rhyming dictionary. Using a given wordlist, a word and the number of ending\n" + \
          "             characters from that word to be matched, returns all the words from the given\n" + \
          "             wordlist that rhyme with the given word with the given precision."
    print "Usage:"
    print "python rhymedict.py [wordlist_file] [word] [precision]\n\n" + \
          "    [wordlist_file]            The wordlist file to be used.\n" + \
          "    [word]                     The word whose ending is to be matched.\n" + \
          "    [precision]                The number of characters from [word] that will be matched.\n" + \
          "    [--help | -h | help]       Show current help text.\n"


class RhymeDictionary():

    """Rhyme dictionary."""

    def __init__(self, wordlist_file):
        """Initialize."""
        self.words = self.get_wordlist(wordlist_file)

    def get_wordlist(self, wordlist_file):
        """Returns a wordlist retrieved from the given file."""
        with open(wordlist_file) as f:
            words = [x.strip('\n') for x in f.readlines()]
        return words

    def get_wordlist_that_rhymes_with(self, word, n):
        """Returns a list of words, whose ending characters match
        the final n characters of the given word."""
        self.matchword = word
        self.precision = int(n)

        pattern = self.matchword[-self.precision:]

        matching_words = [x for x in self.words if x.endswith(pattern)]
        self.remove_word_from_wordlist(self.matchword, matching_words)
        return matching_words

    def remove_word_from_wordlist(self, word, wordlist):
        """Removes given word from wordlist, if the word is included
        in that wordlist."""
        try:
            wordlist.remove(word)
        except ValueError:
            pass

    def print_wordlist(self, wordlist):
        """Prints the given wordlist."""
        for word in wordlist:
            print word

if len(sys.argv) == 4:

    if sys.argv[1] in ["--help", "-h", "help"]:
        print_usage()

    else:
        (wordlist_file, word, precision) = (sys.argv[1], sys.argv[2], sys.argv[3])
        rhyme_dict = RhymeDictionary(wordlist_file)
        matching_wordlist = rhyme_dict.get_wordlist_that_rhymes_with(word, precision)
        rhyme_dict.print_wordlist(matching_wordlist)

else:
    print_usage()
