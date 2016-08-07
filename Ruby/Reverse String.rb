# Reverse String
# for leetcode problems
# 2016.08.07 by zhanglin

# Problem Link:
# https://leetcode.com/problems/reverse-string/

# Problem:
# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".

# @param {String} s
# @return {String}
def reverse_string(s)
  (0..(s.size / 2 - 1)).each do |i|
    s[i], s[s.size - 1 - i] = s[s.size - 1 - i], s[i]
  end

  return s
end


