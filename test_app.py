from app import format_description_as_bullets

def test_format_description_as_bullets():
    text = """
    This is a great toothbrush.
    Made from bamboo.
    Good for the environment.
    """
    expected = "• This is a great toothbrush.\n• Made from bamboo.\n• Good for the environment."
    result = format_description_as_bullets(text)
    assert result == expected
