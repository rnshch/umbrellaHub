from Chapters.ch2.seasons import different_season


def test_the_input_winter():
    assert different_season("winter") == "snow"
