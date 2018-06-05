"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'MY')
    False
    """
    if word in wordlist:
        return True
    return False
        
        


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    """
    row_string=''

    for item in range(len(board[row_index])):
        row_string = row_string + board[row_index][item]
        
    return row_string


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3)
    'TB'
    """
    """new_string = ''
    for letter in board:
        new_string = str(board[0][column_index] + board[1][column_index])
    return new_string"""
    column_string = ''
    for row in board:
        column_string = column_string + row[column_index]
    return column_string


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> board_contains_word_in_row([['T', 'B', 'O', 'V'], ['X', 'O', 'A', 'A']], 'MAY')
    False
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'O', 'S', 'B']], 'NO')
    True
    """
    i = 0
    for column_index in range(len(board[i])):
        if word in make_str_from_column(board, column_index):
            i = i + 1
            return True
        
    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'O', 'S', 'B']], 'NO')
    True
    >>> board_contains_word([['A', 'N', 'X', 'T'], ['X', 'S', 'B', 'V']], 'ANT')
    False
    """
    
    return board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word)
        


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('HELLO')
    5
    """
    points = 0
    
    if len(word) < 3:
        points = 0
    elif 3 <= len(word) <= 6:
        points = points + len(word)
    elif 7 <= len(word) <= 9:
        points = points +(len(word) * 2)
    else:
        points = points + (len(word) * 3)
            
    return points
    


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    ['Jonathan', 7] ANT
    >>> update_score(['Mick', 16], 'DRUDGERY')
    ['Mick', 32] DRUDGERY
    >>> update_score(['Jenn', 0], '')
    ['Jenn', 0] 
    """
    player_info[1] = player_info[1] + word_score(word)
    
    
    
    
    
    
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.


    >>> num_words_on_board([['T', 'B', 'X', 'T'], ['A', 'S', 'O', 'N']], ['ANT', 'BOX', 'SON', 'TO'])
    1
    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    num_words = 0
    for word in words:
        if board_contains_word(board, word):
            num_words = num_words + 1
        
    return num_words


     

def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.

    """
    
    words_list = []

    
    for word in words_file:
        words_list.append(word.rstrip('\n'))
    return words_list
    
    


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    
    board = []
    for line in board_file:
        row = []
        for letter in line.rstrip('\n'):
            row.append(letter)
        board.append(row)
    return board
