#!/bin/bash
cd /outside

make test.exe 2> /dev/null

if [ $? -ne 0 ]
then 
    echo "Compile failed! Can't show output though :("
else
    timeout 10s ./test.exe
fi
