#!/usr/bin/python3
def multiple_returns(sentence):
    return(len(sentence), sentence[0] if len(sentence) > 9 else None)
