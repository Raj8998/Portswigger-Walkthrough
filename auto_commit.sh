#!/bin/bash

if [[ $# -ne 1 ]]
then
	echo "Usage: $0 <commit-message>";
	exit 1;
fi

git add .;
echo "Added to staging";
git commit -m "$1" >> /dev/null 2>> /dev/null;
echo "Commit Done";
git push >> /dev/null 2>> /dev/null;
echo "Pushed to repository";