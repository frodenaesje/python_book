import time
from typing import Dict, List

def brute_force_search(text: str, pattern: str) -> List[int]:
	"""
	Brute force string search algorithm.
	Returns all start indices where pattern occurs in text.
	"""
	if pattern == "":
		return list(range(len(text) + 1))
	if len(pattern) > len(text):
		return []
	
	matches: List[int] = []
	pattern_len = len(pattern)
	text_len = len(text)
	
	for text_pos in range(text_len - pattern_len + 1):
		pattern_pos = 0
		while pattern_pos < pattern_len and text[text_pos + pattern_pos] == pattern[pattern_pos]:
			pattern_pos += 1
		
		if pattern_pos == pattern_len:
			matches.append(text_pos)
	
	return matches


def _build_prefix_table(pattern: str) -> List[int]:
	"""
	Build the prefix table (failure function) for KMP algorithm.
	prefix_table[i] = length of longest proper prefix of pattern[0:i+1]
	that is also a suffix of pattern[0:i+1].
	"""
	pattern_len = len(pattern)
	prefix_table = [0] * pattern_len
	
	# Length of the previous longest prefix suffix
	prefix_len = 0
	pattern_pos = 1
	
	# Build the prefix table
	while pattern_pos < pattern_len:
		if pattern[pattern_pos] == pattern[prefix_len]:
			# Characters match: extend the current prefix
			prefix_len += 1
			prefix_table[pattern_pos] = prefix_len
			pattern_pos += 1
		else:
			# Characters don't match
			if prefix_len != 0:
				# Try with a shorter prefix (backtrack using the table)
				prefix_len = prefix_table[prefix_len - 1]
			else:
				# No prefix found for this position
				prefix_table[pattern_pos] = 0
				pattern_pos += 1
	
	return prefix_table


def kmp_search(text: str, pattern: str) -> List[int]:
	"""
	Knuth-Morris-Pratt string search algorithm.
	Returns all start indices where pattern occurs in text.
	Uses a prefix table to avoid redundant comparisons.
	"""
	if pattern == "":
		return list(range(len(text) + 1))
	if len(pattern) > len(text):
		return []
	
	matches: List[int] = []
	pattern_len = len(pattern)
	text_len = len(text)
	
	# Build the prefix table for the pattern
	prefix_table = _build_prefix_table(pattern)
	
	text_pos = 0
	pattern_pos = 0
	
	# Search through the text
	while text_pos < text_len:
		if pattern[pattern_pos] == text[text_pos]:
			# Characters match: advance both pointers
			text_pos += 1
			pattern_pos += 1
		
		if pattern_pos == pattern_len:
			# Found a complete match
			matches.append(text_pos - pattern_pos)
			# Use prefix table to continue searching for overlapping matches
			pattern_pos = prefix_table[pattern_pos - 1]
		elif text_pos < text_len and pattern[pattern_pos] != text[text_pos]:
			# Mismatch after some matches
			if pattern_pos != 0:
				# Use prefix table to skip already matched characters
				pattern_pos = prefix_table[pattern_pos - 1]
			else:
				# No match at all, move to next character in text
				text_pos += 1
	
	return matches


def _build_bad_char_table(pattern: str) -> Dict[str, int]:
	"""Map each character to its last index in the pattern."""
	table: Dict[str, int] = {}
	for pos, char in enumerate(pattern):
		table[char] = pos
	return table

def boyer_moore_bad_char(text: str, pattern: str) -> List[int]:
	"""
	Boyer-Moore string search using only the bad-character rule.
	Returns all start indices where pattern occurs in text.
	"""
	if pattern == "":
		return list(range(len(text) + 1))
	if len(pattern) > len(text):
		return []

	bad_char = _build_bad_char_table(pattern)
	matches: List[int] = []
	pattern_len = len(pattern)
	text_len = len(text)
	text_pos = 0

	while text_pos <= text_len - pattern_len:
		pattern_pos = pattern_len - 1
		while pattern_pos >= 0 and pattern[pattern_pos] == text[text_pos + pattern_pos]:
			pattern_pos -= 1

		if pattern_pos < 0:
			matches.append(text_pos)
			# Shift by one to continue searching for more matches.
			text_pos += 1
		else:
			last = bad_char.get(text[text_pos + pattern_pos], -1)
			shift = max(1, pattern_pos - last)
			text_pos += shift

	return matches


if __name__ == "__main__":
	text = "ABAAABCDABAAABCDABAAABC"
	pattern = "ABAAABC"

	print(f"Text:    {text}")
	print(f"Pattern: {pattern}\n")

	# Test brute force
	start = time.perf_counter()
	indices_bf = brute_force_search(text, pattern)
	elapsed_bf = time.perf_counter() - start
	print(f"Brute Force:")
	print(f"  Matches at indices: {indices_bf}")
	print(f"  Time: {elapsed_bf * 1000:.4f} ms\n")

	# Test KMP
	start = time.perf_counter()
	indices_kmp = kmp_search(text, pattern)
	elapsed_kmp = time.perf_counter() - start
	print(f"KMP (Knuth-Morris-Pratt):")
	print(f"  Matches at indices: {indices_kmp}")
	print(f"  Time: {elapsed_kmp * 1000:.4f} ms\n")

	# Test Boyer-Moore
	start = time.perf_counter()
	indices_bm = boyer_moore_bad_char(text, pattern)
	elapsed_bm = time.perf_counter() - start
	print(f"Boyer-Moore (Bad Character):")
	print(f"  Matches at indices: {indices_bm}")
	print(f"  Time: {elapsed_bm * 1000:.4f} ms")
