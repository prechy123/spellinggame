import pytest
from spellinggame import get_user_difficulty, select_eight_words, word_to_audio

def test_get_user_difficulty():
    assert get_user_difficulty(1) == "Beginner"
    assert get_user_difficulty(4) == "Expert"
    assert get_user_difficulty(5) == "Impossible"
    with pytest.raises(ValueError):
        get_user_difficulty(10)
    
def test_select_eight_words():
    result1 = select_eight_words(['Cat', 'Dog', 'Sun', 'Hat', 'Run', 'Big', 'Cup', 'Red', 'Pen', 'Bed', 'Box', 'Fox', 'Cake', 'Book', 'Fish', 'Sock', 'Chair', 'Leaf', 'Moon', 'Star', 'Car', 'Tree', 'Ball', 'Ship', 'Key', 'Door', 'Cow', 'Snow', 'Leaf', 'Moon', 'Star', 'Car', 'Tree', 'Ball', 'Ship', 'Key', 'Door', 'Cow', 'Snow', 'Leaf', 'Moon', 'Star', 'Car', 'Tree', 'Ball', 'Ship', 'Key', 'Door', 'Cow', 'Snow'])
    assert len(result1) == 8
    result2 = select_eight_words(['Hippopotomonstrosesquipedaliophobia', 'Supercalifragilisticexpialidocious', 'Antiestablishmentarianism', 'Pneumonoultramicroscopicsilicovolcanoconiosis', 'Parastratiosphecomyiastratiosphecomyioides', 'Floccinaucinihilipilification', 'Antitransubstantiationalistically', 'Microspectrophotometrically', 'Indistinguishableness', 'Overintellectualization', 'Pharmacopoeiist', 'Hippopotamus', 'Incomprehensibilities', 'Polyphiloprogenitive', 'Honorificabilitudinitatibus', 'Supercalifragilisticexpialidoses', 'Electroencephalographically', 'Pseudopseudohypoparathyroidism', 'Immunoelectrophoretically', 'Thyroparathyroidectomized'])
    assert len(result2) == 8
    
def test_word_to_audio():
    assert word_to_audio("book") == "success"
    assert word_to_audio("Cat") == "success"