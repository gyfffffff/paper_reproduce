import os
path = r'data\tweet\preprocessed'
srcnames = os.listdir(path)
for srcname in srcnames:
    os.rename(os.path.join(path, srcname), os.path.join(path, srcname[:6]))