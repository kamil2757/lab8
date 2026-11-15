words = ["bananaffff", "ШАМПАНЗЕ", "скебоб", "абоба", "борик", "Марвел"]
sorted_words = sorted(words, key=lambda x: (len(x), x))
print(sorted_words)