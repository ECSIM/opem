#!/bin/bash

PIP=`which pip || (python --version 2>&1 | grep -q 'Python 2' && which pip2) || (python --version 2>&1 | grep -q 'Python 3' && which pip3)`

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    brew install pyenv >> /dev/null
    brew update && brew upgrade pyenv
    case "${TOXENV}" in
        py34)
            pyenv install 3.4.9
	    pyenv global 3.4.9
	    ;;
        py35)
            pyenv install 3.5.6
	    pyenv global 3.5.6
            ;;
	py36)
            pyenv install 3.6.7
	    pyenv global 3.6.7
	    ;;
	py37)
            pyenv install 3.7.1
	    pyenv global 3.7.1
	    ;;
	*)
	    brew upgrade python
	    ;;
    esac
fi
