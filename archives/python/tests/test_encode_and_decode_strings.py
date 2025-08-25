from problems.medium.encode_and_decode_strings import Codec

codec = Codec()


def test_sample_simple():
    dummy_input = ["Hello", "World"]
    assert codec.decode(codec.encode(dummy_input)) == dummy_input


def test_sample_one_empty_string():
    dummy_input = [""]
    assert codec.decode(codec.encode(dummy_input)) == dummy_input


def test_sample_two_empty_string():
    dummy_input = ["", ""]
    assert codec.decode(codec.encode(dummy_input)) == dummy_input
