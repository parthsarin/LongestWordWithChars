#!/usr/bin/env python3
"""
Generates a list of words which contain a specified
number of characters in a particular order.
"""
class TopK:
	def __init__(self, k=3, key=lambda x: x):
		self.key = key
		self.max_val = 0

		self.k = k
		self.elems = []

	def push(self, val):
		if self.key(val) > self.max_val:
			self.max_val = self.key(val)
			self.elems.append(val)
			self.elems.remove(min(self.elems, key=self.key))

		elif len(self.elems) < self.k:
			self.elems.append(val)

	def pop(self):
		output = max(self.elems, key=self.key)
		self.elems.remove(output)
		return output

	def dump(self):
		return sorted(self.elems, key=self.key)[::-1]

	def __nonzero__(self):
		return self.elems

	def __len__(self):
		return len(self.elems)

def get_words():
	with open('/usr/share/dict/words', 'r') as f:
		words = f.read().lower()

	words = list(set(words.split('\n')[:-1]))
	return words

def is_match(word, chars):
	if chars:
		if word:
			i = word.find(chars[0])
			if i == -1:
				return False
			else:
				remaining_word = word[i+1:]
				remaining_chars = chars[1:]
				return is_match(remaining_word, remaining_chars)
		else:
			# There are still characters to search for but no word remaining
			return False
	else:
		return True

def main():
	words = get_words()
	K_TOP_HITS = 3

	while True:
		chars = input("Characters to search for? ").lower()

		hits = []
		for word in words:
			if is_match(word.lower(), chars):
				hits.append(word)

		top_hits = TopK(k=K_TOP_HITS, key=len)
		for hit in hits:
			top_hits.push(hit)

		if top_hits:
			print("Longest matching words:")
			for i in range(len(top_hits)):
				print(f"Hit #{i+1}: {top_hits.pop()}")
		else:
			print("No matching words found.")

		print()

if __name__ == '__main__':
	main()