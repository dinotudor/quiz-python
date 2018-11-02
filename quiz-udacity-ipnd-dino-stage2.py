# encoding=utf8

#declare variables, lists and strings to be used

# simple quiz, fill in the gaps. Part of graduation in Udacity Nanodegree, intro to programming in 2018

import sys

questions = ['___1___ is a great country. Its capital is ___2___. People speak ___3___. Their biggest airport is located in Frankfurt. ___4___ is home to a famous Beer festival called Oktober Fest.',
'___1___ is the largest ___2___ in South America. It won the first World Cup in ___3___. The most iconic player at that time was Edson Arantes do Nascimento, also known as ___4___.',
'Python is the ___1___ most used programming language now adays. A ___2___ is used to take ___3___ and produce ___4___.']

gaps = ['___1___','___2___','___3___','___4___']

answers = [['Germany','Berlin','german','Munich'],['Brazil','country','1958','Pele'],['fifth','procedure','inputs','outputs']]

level_select = ['easy','medium','hard']

level_dictionary = {'easy' : questions[0],
                    'medium' : questions[1],
                    'hard' : questions[2]}

messages = [['Great! Lets move on! '],['Oops! wrong answer...try again: '],['This is  how the phrase looks now: ---- >'],['Congratulation! You made it! Hope you had a great time playing! ']]

messages_separador = 150
hello_statement_lenght = len('Hello! Welcome to the fill in the Gaps game! You must guess the missing words in the gaps to complete the game!')

# inicio jogo

print '#'* hello_statement_lenght
print('Hello! Welcome to the fill in the Gaps game! You must guess the missing words in the gaps to complete the game!')
print '#'* hello_statement_lenght
choose_level = ''
how_many_tries = ''

def game_choices():
    """
    Usuario optar pelo nivel do jogo
    in - nivel de dificuldade
    out - variavel global choose_level com nivel escolhido
    """
    global choose_level
    choose_level = raw_input('Please choose one dificulty level: (easy, medium or hard) ')
    choose_level = choose_level.lower()
    if choose_level in level_select:
        return choose_level
    else:
        while choose_level not in level_select:
            choose_level = raw_input('Invalid option, please try again: (easy, medium, hard)')
            choose_level = choose_level.lower()
        return choose_level

game_choices()

def how_many_turns():
    """
    Usuario optar pelo numero de tentativas
    in - integer de 1 a 9
    out - variavel global how_many com numero escolhido
    """
    global how_many
    max_tries = 9
    positive_numbers = 0
    how_many = int(raw_input('How many turns you want to try each gap? (from 1 to 9) '))
    if how_many <= max_tries and how_many > positive_numbers:
        return how_many
    else:
        while how_many > max_tries or how_many <= positive_numbers:
            how_many = int(raw_input('Not valid option. Try again, choose a number from 1 to 9: '))
        return how_many

how_many_turns()

def load_level(a):
    """
    carregar frase e conjunto de respotas dentro de um dicionario
    in - choose_level
    out - set com pergunta e respostas
    """
    global choose_level
    if choose_level == 'easy':
        return level_dictionary['easy']
    elif choose_level == 'medium':
        return level_dictionary['medium']
    elif choose_level == 'hard':
        return level_dictionary['hard']

print '\n'*1 + '-' * messages_separador + '\n'*1
print load_level(choose_level)
print '\n'*1 + '-' * messages_separador + '\n'*1


def check_answers():
    """
    funcao auxiliar para identificar set de respostas
    in - choose_level
    out - respostas do quiz de acordo com o nivel de selecao
    """
    global choose_level
    if choose_level == 'easy':
        return answers[0]
    elif choose_level == 'medium':
        return answers[1]
    elif choose_level == 'hard':
        return answers[2]

check_answers()

def word_in_pos(word, parts_of_speech):
    """
    funcao auxiliar usada no madlibs generator, nao e minha autoria
    in - questions e gaps
    out - palavra a ser substituida no quiz ou strings a serem adicionadas na lista que ira se torna a frase toda
    """
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def check_correct_gap(a):
    """
    funcao auxiliar para conferir se a resposta esta correta
    in (globals) - user_input, check_answers
    out - variavel com a 'string' correta para ser adicionada na funcao play_game
    """
    global checked
    global user_input
    global how_many
    count = 1
    check_set = check_answers()
    checked = user_input
    #checked = checked.lower()
    while checked not in check_set:
        checked = raw_input(messages[1])
        #checked = checked.lower()
        count += 1
        if count > how_many:
            print '#' * messages_separador
            sys.exit('----- > Game Over!! You missed '+ str(how_many) +" times as you choosen before! < -----")
    else:
        print '\n'*1 + '_' * messages_separador + '\n'*1
        print(messages[0])
        return checked
    return checked

def play_game(gaps_number, gaps_numbers):
    """
    funcao usada no madlibs generator adaptada para rodar no quiz
    input - user input(resposta do quiz), how_many(selecao de nivel), checked(resposta conferida)
    out - nova string
    """
    global user_input
    global replacement
    global checked
    global how_many
    global gaps_to_fill
    replaced = []
    gaps_to_fill = load_level(choose_level)
    gaps_to_fill = gaps_to_fill.split()
    for word in gaps_to_fill:
        replacement = word_in_pos(word, gaps_numbers)
        if replacement != None:
            user_input = raw_input("Fill in the GAP " + replacement + " ")
            checked = check_correct_gap(user_input)
            word = word.replace(replacement, checked)
            replaced.append(word)
            gaps_to_fill = " ".join(gaps_to_fill)
            gaps_to_fill = gaps_to_fill.replace(replacement, checked)
            print '\n'*1 + '#' * messages_separador + '\n'*1
            print gaps_to_fill
            gaps_to_fill = gaps_to_fill.split()
            print '\n'*1 + '#' * messages_separador + '\n'*1
        else:
                replaced.append(word)
    replaced = " ".join(replaced)
    print messages[3]
    print '\n'*1 + '#' * messages_separador + '\n'*1
    return replaced
    print '\n'*1 + '#' * messages_separador + '\n'*1

print play_game(choose_level, gaps)
