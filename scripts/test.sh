#!/bin/bash
echo "Submit last updated file"
file_name=$(find . -type f -print0 | xargs -0 stat -f "%m %N" | sort -rn | head -1 | cut -f2- -d" ")
echo "$file_name"
leetcode test $file_name
