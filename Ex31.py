import re
def text_match(text):
 patterns = 'ab+?'
 if re.search(patterns, text):
  return 'Found a match!'
 else:
  return('Not matched!')
print(text_match("ab"))
print(text_match("abc"))
print(text_match("a computer"))
