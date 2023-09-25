import project1

input22 = """
,
    .
?
    (
)
    :::
:-

,.?()::-"""

answer22 = '''(COMMA,",",2)
(PERIOD,".",3)
(Q_MARK,"?",4)
(LEFT_PAREN,"(",5)
(RIGHT_PAREN,")",6)
(COLON,":",7)
(COLON,":",7)
(COLON,":",7)
(COLON_DASH,":-",8)
(COMMA,",",10)
(PERIOD,".",10)
(Q_MARK,"?",10)
(LEFT_PAREN,"(",10)
(RIGHT_PAREN,")",10)
(COLON,":",10)
(COLON_DASH,":-",10)
(EOF,"",12)
Total Tokens = 17'''

def test_project1():
    assert project1.project1(input22) == answer22
