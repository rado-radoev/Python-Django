import re
def verify(isbn):
    # no_dashesh_isbn = re.sub(r'[^A-Za-z]', "", isbn).lower()
    # is_last_char_x = re.match()
    # match_any_char_but_x = re.search(r'(?![xX])[A-Za-z]$')
    #
    # '''
    #     Check if the length of the ISBN si more than 10 chars
    #
    # '''
    # if match_any_char_but_x or len(no_dashesh_isbn) != 10:
    #     return False

    return re.search(r'(ISBN[-]*(1[03])*[ ]*(: ){0,1})*(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10})', isbn)



