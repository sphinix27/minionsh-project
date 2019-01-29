from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from navigationstack.navigation_stack import NavigationStack

custom_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


def ask_action():
    actions = {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Add',
            Separator(),
            'Undo',
            'Redo',
            'Exit'
        ]
    }

    choice = prompt(actions, style=custom_style)
    return choice['action']


def get_input():
    item = {
        'type': 'input',
        'name': 'add',
        'message': 'Input the Item to Add?',
    }
    return prompt(item, style=custom_style)


def main():
    navigation_stack = NavigationStack()
    exit_cli = False
    while not exit_cli:
        action = ask_action()
        if 'Add' == action:
            navigation_stack.add(get_input().get('add'))
        elif 'Undo' == action:
            navigation_stack.undo()
        elif 'Redo' == action:
            navigation_stack.redo()
        elif 'Exit' == action:
            exit_cli = True
        pprint(navigation_stack.redo_stack.stack)


if __name__ == '__main__':
    main()
