#!/bin/sh

LOGDIR="${WORKSPACE}/target"

export PYTHONPATH="$PWD:$PYTHONPATH"

# make our build log dir
mkdir -p "${LOGDIR}"

# enter source
cd "${WORKSPACE}"

# lint tests
pylint --rcfile=.pylintrc lessons > "${LOGDIR}/pylint.log"

# unit tests
nosetests -w test/unit/ --with-xunit --xunit-file="${LOGDIR}/nosetest.xml"

