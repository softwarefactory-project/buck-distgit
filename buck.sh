#!/bin/sh

export PYTHONPATH=/usr/libexec/buck/third-party/nailgun
exec /usr/libexec/buck/programs/buck.py "$@"
