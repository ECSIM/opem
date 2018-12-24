PIP=`which pip || (python --version 2>&1 | grep -q 'Python 2' && which pip2) || (python --version 2>&1 | grep -q 'Python 3' && which pip3)`

# Install Python3 on osx
if [ "$TRAVIS_OS_NAME" = "osx" ] && [ ! -z "$TOXENV" ]
then
  $PIP install --user -U tox
  brew install python3
  exit 0
fi

