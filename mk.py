from glob import glob

def resplit(a):
  return '/'.join(a.split('/')[1:])


def main(arg):

  pref = arg[1]

  for font, img in zip(sorted(glob(pref+'font/*')), sorted(glob(pref+'img/*'))):
    f = resplit(font)
    i = resplit(img)
    print('![{:s}]({:s}?raw=true \'font\')'.format(f, i))
    print('[{:s}]({:s})'.format(f, f))


if __name__ == '__main__':
  from sys import argv
  main(argv)


