class ReadingLevelTracker:
	
	def __init__(self, total_words, total_sentences, total_syllables):
		self.total_words = total_words
		self.total_sentences = total_sentences
		self.total_syllables = total_syllables

	def read_file(self, filename):
		with open(filename, 'r') as myfile:
			data = myfile.read().replace('\n', '')
		return data

	def find_information(self, text_string):
		self.num_words_in_document(text_string)
		self.num_sentences_in_document(text_string)

	def num_words_in_document(self, text_string):
		for word in text_string.split():
			self.total_words += 1
		print("Total words:     ", self.total_words)

	def num_sentences_in_document(self, text_string):
		self.total_sentences += text_string.count('.')
		self.total_sentences += text_string.count('!')
		self.total_sentences += text_string.count('?')
		self.total_sentences -= 3 * text_string.count('...')
		print("Total sentences: ", self.total_sentences)

	def find_syllables_in_word(self):
		print("Syllables in word")

	def find_syllables_in_sentence(self):
		print("Syllables in sentence")

	def find_syllables_in_file(self):
		print("Syllables in file")

example = ReadingLevelTracker(0, 0, 0)
text_string = example.read_file('test.txt')
example.find_information(text_string)