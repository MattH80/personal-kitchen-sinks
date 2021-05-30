import subprocess
import sys

process = subprocess.Popen([sys.executable, r'PythonCode\commtest2.py'], stdin=subprocess.PIPE, 
                            stdout=subprocess.PIPE, bufsize=0)
for _ in range(3):
    process.stdin.write(b'hello\r\n')
    print(process.stdout.readline())

    