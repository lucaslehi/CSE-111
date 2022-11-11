from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest
quantity = 1
tense = 'past'

def test_get_determiner():
    
    single_determiners = ["a", "the", "one"]

    for _ in range(4):
        word = get_determiner(1)

        assert word in single_determiners

    plural_determiners = ["two","some", "many","the"]
    for _ in range(4):
        
        
        word = get_determiner(2)

        assert word in plural_determiners

def test_get_noun():
   
    singular_determiners = [ "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    
    for _ in range(4):
        word = get_noun(1)

        assert word in singular_determiners

   
    plural_determiners = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)

        assert word in plural_determiners

def test_get_verb():

    if_one = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote","drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes", "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        word = get_verb(1, 'past')

        assert word in if_one


def test_get_preposition():

    singular_determiners = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]

    for _ in range(4):
        word = get_preposition()

        assert word in singular_determiners


def test_get_prepositional_phrase():
    assert len(str(get_prepositional_phrase(quantity)).split(' ')) == 3

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])