import pip

def install(package):
    pip.main(['install',package])

install('beautifulsoup4')
install('nltk')
