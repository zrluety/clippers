import sys


def choice_prompt(prompt, choices):
    # create a check box for each choice
    choice_list = []
    choice_index = 0

    for index, choice in enumerate(choices):
        if index == choice_index:
            list_str = "[x] {}".format(choice)
        else:
            list_str = "[ ] {}".format(choice)

        choice_list.append(list_str)

    choice_list_str = "\n".join(choice_list)
    sys.stdout.write(prompt + "\n" + choice_list_str)