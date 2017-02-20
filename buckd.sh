#!/bin/sh

export PYTHONPATH=/usr/libexec/buck/third-party/nailgun
exec /usr/libexec/buck/programs/buckd.py "$@"
