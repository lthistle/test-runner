#!/bin/bash
cd /outside

if [ -f "test.exe" ]; then
    echo "Running binary..."
    timeout -k 1 10 ./test.exe
    if [ $? -eq 124 ]
    then
        echo "Test case timed out :("
    fi
fi
