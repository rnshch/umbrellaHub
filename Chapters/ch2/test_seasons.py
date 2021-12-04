from Chapters.ch2.seasons import different_season


def test_the_input_winter(monkeypatch):
    input1 = "winter"
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda x: input1)
        assert different_season() == "snow"
