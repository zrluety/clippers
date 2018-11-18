import textwrap

import clippers

from pynput.keyboard import Key, Controller


def test_choice_prompt(capsys):
    # Given a prompt and list of choices the user should see the prompt
    # followed by a list of choices with a check box beside each choice.
    prompt = "Which house do you belong to?"
    choices = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    expected_out = textwrap.dedent(
        """\
        Which house do you belong to?
        [x] Gryffindor
        [ ] Slytherin
        [ ] Ravenclaw
        [ ] Hufflepuff"""
    )
    clippers.choice_prompt(prompt, choices)
    captured = capsys.readouterr()
    assert captured.out == expected_out