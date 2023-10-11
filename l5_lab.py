import re

text = ['We live in the state of Illinois.',
        'Bob lives in a state of denial.',
        'My parents live in the state of Michigan.',
        'It is super hot in the state of Florida!',
        'I used to live in the state of California.']

pattern = r"state of ([A-Z][\w]+)"
print(re.search(pattern, text[0]))

re_results = [re.search(pattern, t) for t in text]
print(re_results)

print([res for res in re_results])
print([res for res in re_results if res])
print([res.group(1) for res in re_results if res])

data = ['USA IL 2020 10 1000',
        'USA CA 2020 11 2000',
        'CAN QC 2020 08 3000']

def parse_line(l):
    #extract the data out of a line of text/html/etc
    country, st, year, val1, val2 = l.split(' ')
    return [country, st, year, val1, val2]

lines = [parse_line(line) for line in data]
lines = [','.join(line) for line in lines]
doc = '\n'.join(lines)

with open('my_doc.csv', 'w') as ofile:
    ofile.write(doc)