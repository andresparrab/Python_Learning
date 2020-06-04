import subprocess

# subprocess.call('ls', shell=True)
output = subprocess.check_output('ls -la', shell=True)

print(output)