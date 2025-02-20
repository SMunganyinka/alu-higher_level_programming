#!/usr/bin/python3


def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
