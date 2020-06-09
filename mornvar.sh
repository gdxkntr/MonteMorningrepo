#!/bin/bash

greeting="welcome"

user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! today is $day which is the best day of the week."
echo "your bash shell version is: $BASH_VERSION cool!"

