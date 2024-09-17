import subprocess                                                                                                                                              
# From Python3.7 you can add
# keyword argument capture_output
text = str(subprocess.run(["setxkbmap", "-query"], capture_output=True))
language = text.split('\\') 
if language[2] == 'nlayout:     ru':
    subprocess.run(["setxkbmap", "-layout", "cz", "-variant", "coder"])
elif language[2] == 'nlayout:     cz':
    subprocess.run(["setxkbmap", "-layout", "ru", "-variant", "phonetic"])
else:
    subprocess.run(["setxkbmap", "-layout", "cz", "-variant", "coder"])
