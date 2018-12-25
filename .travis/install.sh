#!/bin/bash
if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
	pip3 install tox
    case "${TOXENV}" in
        py34-osx)
        pyenv install 3.4.8
	    pyenv global 3.4.8
	    ;;
        py35-osx)
        pyenv install 3.5.5
	    pyenv global 3.5.5
            ;;
	    py36-osx)
        pyenv install 3.6.5
	    pyenv global 3.6.5
	    ;;
	    py37-osx)
        pyenv install 3.7.0b3
	    pyenv global 3.7.0b3
	    ;;
	*)
	    brew upgrade python
	    ;;
    esac

	exit 0
fi
pip install -r requirements.txt
python setup.py install
# Make sure tox is installed and up to date
pip install -U tox