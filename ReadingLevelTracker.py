class ReadingLevelTracker:

    def __init__(self, total_words, total_sentences, total_syllables):
        self.total_words = total_words
        self.total_sentences = total_sentences
        self.total_syllables = total_syllables
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.specials = ["ia"]
        self.specials_except_end = ["ie","ya","es","ed"]

    def read_file(self, filename):
        with open(filename, 'r') as myfile:
            data = myfile.read().replace('\n', '')
        return data

    def find_information(self, text_string):
        self.num_words_in_document(text_string)
        self.num_sentences_in_document(text_string)
        self.num_syllables_in_document(text_string)

    def num_words_in_document(self, text_string):
        for word in text_string.split():
            self.total_words += 1
        print("Total words:       ", self.total_words)

    def num_sentences_in_document(self, text_string):
        self.total_sentences += text_string.count('.')
        self.total_sentences += text_string.count('!')
        self.total_sentences += text_string.count('?')
        self.total_sentences -= 3 * text_string.count('...')
        print("Total sentences:   ", self.total_sentences)

    def num_syllables_in_document(self, text_string):
        for word in text_string.split():
            self.total_syllables += self.find_syllables_in_word(word)
        print("Total syllables:   ", self.total_syllables)

    def find_syllables_in_word(self, word):
        self.current_word = word.lower()
        self.num_syllables = 0
        self.last_was_vowel = False
        self.last_letter = ""

        self.iterate_word(word)
        self.handle_special_cases(word)

        return self.num_syllables

    def iterate_word(self, word):
        for letter in self.current_word:
            if letter in self.vowels:
                #don't count diphthongs unless special cases
                combo = self.last_letter + letter
                if self.last_was_vowel and combo not in self.specials and combo not in self.specials_except_end:
                    self.last_was_vowel = True
                else:
                    self.num_syllables += 1
                    self.last_was_vowel = True
            else:
                self.last_was_vowel = False

            self.last_letter = letter

        return self.num_syllables

    def handle_special_cases(self, word):
        #handle cases for "ie","ya","es","ed"
        if len(self.current_word) > 2 and self.current_word[-2:] in self.specials_except_end:
            self.num_syllables -= 1

        #remove silent single e but not ee since it counted it before
        elif len(self.current_word) > 2 and self.current_word[-1:] == "e" and self.current_word[-2:] != "ee":
            self.num_syllables -= 1

    def calculate_reading_level(self):
        FIRST_CONSTANT = 206.835
        SECOND_CONSTANT = 1.015
        THIRD_CONSTANT = 84.6
        self.reading_level = FIRST_CONSTANT - SECOND_CONSTANT * \
                            (self.total_words / self.total_sentences) - THIRD_CONSTANT * \
                            (self.total_syllables / self.total_words)

        return self.reading_level

example = ReadingLevelTracker(0, 0, 0)
text_string = example.read_file('book.txt')
example.find_information(text_string)
print("Score:             ", example.calculate_reading_level())
