import subprocess
while True:
    subprocess.run("python3 scrapper.py & python3 server.py",shell=True)
