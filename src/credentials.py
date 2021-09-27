__name__ = 'credentials'
__author__ = 'jeroen.weber@hu.nl'


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    #print('I am being imported from another module')
    pass

def getcredentials(user):
    if (user == 'jeroen.weber@hu.nl'):
        return 'f1f9badee1de422eadbd86fd0eacf59f'

def getprimary(user):
    if (user == 'jeroen.weber@hu.nl'):
        return 'cd5f72b21d9b4411b28174a16f8cd68b'
