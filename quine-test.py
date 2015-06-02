import subprocess
from io import StringIO
with open('quine.py', 'r') as file:
	text = file.read().replace('\r\n', '\n')
	
out = subprocess.check_output(['python', 'quine.py']).decode('raw-unicode-escape').replace('\r\n', '\n')
print(out)
print(text == out)

if text == out:
  print('Good:')
  print(out)
else:
  for i in range(0, len(out)):
    print(i, out[i], text[i], out[i] == text[i])
 