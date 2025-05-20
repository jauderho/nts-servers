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

# Run the chronyd command with the argument
chronyd -Q -t 5 "server $NTS_SERVER iburst nts maxsamples 1"
