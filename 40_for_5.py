line = "the easylearn academy 105, eva surbhi opp waghawadi road, bhavnagar - 36001"

words = 0
letters = 0
digits = 0
symbols = 0
inside_word = False

for char in line:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    elif not char.isspace():
        symbols += 1

    if char.isspace():
        inside_word = False
    elif not inside_word:
        words += 1
        inside_word = True

print(f"No. of words: {words}")
print(f"No. of letters: {letters}")
print(f"No. of digits: {digits}")
print(f"No. of symbols: {symbols}")