#!/bin/bash

PIP=`which pip || (python --version 2>&1 | grep -q 'Python 2' && which pip2) || (python --version 2>&1 | grep -q 'Python 3' && which pip3)`

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    pyenv install -l
    case "${TOXENV}" in
        py34)
            pyenv install 3.4.8
	    pyenv global 3.4.8
	    ;;
        py35)
            pyenv install 3.5.5
	    pyenv global 3.5.5
            ;;
	py36)
            pyenv install 3.6.5
	    pyenv global 3.6.5
	    ;;
	py37)
            pyenv install 3.7.0b3
	    pyenv global 3.7.0b3
	    ;;
	*)
	    brew upgrade python
	    ;;
    esac
fi
