blues_file = open('programmers_blues.txt')

# reading in the file
blues_content = blues_file.read()

# clean up the text
blues_content = blues_content.replace('.', '')
blues_content = blues_content.replace(',', '')
blues_content = blues_content.replace('!', '')
blues_content = blues_content.replace('(', '')
blues_content = blues_content.replace(')', '')

# split text into words
blues_word_list = blues_content.lower().split()

# tally the words
counts = {}

for word in blues_word_list:
    current_tally = counts.get(word, 0)
    new_tally = current_tally + 1
    counts[word] = new_tally


entries = counts.items()

# version 1 - sorts by what mykey says in the value in the tuple to sort by
# def mykey(entry):
#     return entry[1]
# entries.sort(key=mykey, reverse=True)

# version 2 - same as #1, but uses destructuring syntax in the function parameter
# def mykey((word, count)):
#     return count
# entries.sort(key=mykey, reverse=True)

# version 3 - same as #1 but uses a lambda short hand instead of a def statement to define a function
# entries.sort(key=lambda entry: entry[1], reverse=True)

# version 4 - same as #3 but uses destructuring syntax in the lambda parameter
#entries.sort(key=lambda (word, count): count, reverse=True)

# version 5 - sorting the dictionary directly
top_10 = sorted(counts, key=counts.get, reverse=True)[:10]
for word in top_10:
    count = counts[word]
    print "%s appeared %d times." % (word, count)

# version 1-4 use the below code to print
# top_10 = entries[:10]
# for word, count in top_10:
#     print "%s appeared %d times." % (word, count)
