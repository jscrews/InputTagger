import difflib

with open('input/test.txt', 'r') as inputFile:
  with open('output/test.txt', 'r') as outputFile:
    diff = difflib.unified_diff(
      outputFile.readlines(),
      inputFile.readlines(),
      fromfile='outputFile',
      tofile='inputFile'
    )
    for line in diff:
      if line[0:3] == "+++" or line[0:3] == "---" or line[0:2] == "@@":
        print(line)
"""       if line[0] is '+':
        print(line) """