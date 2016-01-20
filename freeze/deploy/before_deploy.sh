#!/bin/bash

# Create archive dist/shub-linux.tar.gz (or dist/shub-osx.tar.gz) containing
# only the shub binary (and no directory structure)
tar -czf dist/shub-${TRAVIS_OS_NAME}.tar.gz -C dist shub
