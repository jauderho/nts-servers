#!/bin/bash
#
# h/t https://github.com/cadusilva
#

# Check if argument is passed
if [ -z "$1" ]; then
  echo "Usage: $0 <NTS_SERVER>"
  exit 1
fi

# Assign the argument to a variable
NTS_SERVER=$1

# Prefer rkik if available, fall back to chronyd
if command -v rkik &>/dev/null; then
  rkik --nts "$NTS_SERVER"
else
  chronyd -Q -t 5 "server $NTS_SERVER iburst nts maxsamples 1"
fi
