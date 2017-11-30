
from glob import glob

for f, i in zip(sorted(glob('font/*')), sorted(glob('img/*'))):
    print('![{:s}]({:s}?raw=true \'font\')'.format(f, i))
    print('[{:s}]({:s})'.format(f, f))

