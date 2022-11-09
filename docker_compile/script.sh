#!/bin/bash
cd ./outside

timeout -k 1 10 make test.exe 2> /dev/null
if [ $? -ne 0 ]
then
    echo "Compile failed! Can't show output though :("
else 
    mv test.exe bin/test.exe
fi
