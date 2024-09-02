class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r') as file:
                words = []
                for j in file:
                    j = j.lower()
                    sign = [',', '.', '=', '!', '?', ';', ':']
                    for k in sign:
                        j = j.replace(k, '')
                    j = j.replace(' - ', ' ')
                    words.extend(j.split())
                all_words[i] = words
        return all_words

    def find(self, word):
        word_position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                word_position[key] = value.index(word.lower()) + 1

        return word_position

    def count(self, word):
        word_quantity = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            word_quantity[value] = words_count

        return word_quantity


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
