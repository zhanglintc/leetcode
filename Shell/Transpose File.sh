# Transpose File
# for leetcode problems
# 2015.07.01 by zhanglin

# Problem Link:
# https://leetcode.com/problems/transpose-file/

# Problem:
# Given a text file file.txt, transpose its content.

# You may assume that each row has the same number of columns and each field is separated by the ' ' character.

# For example, if file.txt has the following content:

# name age
# alice 21
# ryan 30
# Output the following:

# name alice ryan
# age 21 30

# Read from the file file.txt and print its transposed content to stdout.
awk '{
    for(i = 1; i <= NF; i++) {
        m[NR, i] = $i;
    }
}

END {
    for(i = 1; i <= NF; i++) {
        line = m[1, i];
        for(j = 2; j <= NR; j++) {
            line = line" "m[j, i];
        }
        print line;
    }
}' file.txt


