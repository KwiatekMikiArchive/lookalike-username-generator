import exrex
import re

username = input("> ")
regexuser = username.lower()
regexuser = re.sub(r'[il1]', '[il1]', regexuser)
regexuser = re.sub(r'[o0]', '[o0]', regexuser)
regexuser = re.sub(r'[uv]', '[uv]', regexuser)
regexuser = re.sub(r'[sz]', '[sz]', regexuser)
all = list(exrex.generate(regexuser))

print('\n'.join(all))
print("Combinations generated: " + str(len(all)))
