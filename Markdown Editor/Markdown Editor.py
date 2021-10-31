def plain():
    return input('Text: ')


def bold():
    return f'**{input("Text: ")}**'


def italic():
    return f'*{input("Text: ")}*'


def header():
    while True:
        level = int(input('Level: '))
        if level not in range(1, 7):
            print('The level should be within the range of 1 to 6')
        else:
            break
    return f'{"#" * level} {input("Text: ")}\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def code():
    return f'`{input("Text: ")}`'


def new_line():
    return '\n'


def o_list():
    global user
    line = []
    while True:
        row = int(input('Number of rows: '))
        if row < 1:
            print('The number of rows should be greater than zero')
        else:
            for x in range(1, row + 1):
                line.append(input(f'Row #{x}: '))
            for y in range(0, len(line)):
                if user == 'ordered-list':
                    line[y] = f'{y + 1}. {line[y]}\n'
                elif user == 'unordered-list':
                    line[y] = f'* {line[y]}\n'
            return ''.join(line)


forms = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header, 'link': link, 'inline-code': code,
         'new-line': new_line, 'ordered-list': o_list, 'unordered-list': o_list}
output = ''

while True:
    user = input('Choose a formatter: ')
    if user == '!done':
        file = open('output.md', 'w', encoding='utf-8')
        file.writelines(output)
        file.close()
        break
    elif user == '!help':
        print('Available formatters:', ' '.join(forms))
        print('Special commands: !help !done')
    elif user in forms.keys():
        output += forms[user]()
        print(output)
    else:
        print('Unknown formatting type or command')
