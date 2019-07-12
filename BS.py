'''program for making from 3 words another word, which contain from first, center and last letter each of this words '''

class Word:
    __slots__ = 'word_start','word_center','word_end','word'

    def _word_start_(self,word):
        self.word_start = word[0]

    def _word_end_(self,word):
        self.word_end =word[-1]

    def _word_center_(self,word):
        self.word_center = word[len(word)/2]

    def __init__(self, word):
        self.word = word
        self._word_start_(word)
        self._word_end_(word)
        self._word_center_(word)

Statement = Word("Statement")
Pytthon = Word("Pytthon")

Books= Word("Books")

def main_foo(first_obj,second_obj,third_obj):
    string = ""
    obj_list = [first_obj,second_obj,third_obj]
    dict_todo = {0:'word_start', 1: 'word_center', 2: 'word_end'}

    for i in range(3):
        for item in obj_list:
            string += item.__dict__[dict_todo[i]]
    return string
print(main_foo(Statement,Pytthon,Books))
