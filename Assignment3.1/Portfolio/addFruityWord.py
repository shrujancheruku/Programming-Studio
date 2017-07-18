from mongoengine import *
from schemas import FruityWord
"""
Script to add a new expletive to the db. Simply replace the
parameters in the Document initialization and run the script
"""


connect('assignment3db')
new_word = FruityWord(fruity_word="douche", less_fruity_word="french elitist back scrubber")
new_word.save()