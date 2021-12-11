import pytest
from compress import compress_str 

class TestCompress:
    """
    Unit tests for the compress feature
    """
    
    def test_compress_string(self):
        """
        Test the happy path compressing the input according to the requested
        functionality.
        """

        input_string = "aaabbbccc"
        expected_output = "a3b3c3"

        output = compress_str(input_string)

        assert output == expected_output

    def test_compress_string_with_numbers(self):
        """
        Test the input string containing numbers according to the requested
        functionality.
        """

        input_string = "aaabbbccc12az"
        expected_output = "a4b3c31121z1"

        with pytest.raises(ValueError):
            output = compress_str(input_string)


