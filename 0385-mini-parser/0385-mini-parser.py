# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        if len(s) <= 2:
            return NestedInteger()
        stack, num, sign = [], 0, 1
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '-':
                sign = -1
            elif s[i] == '[':
                stack.append(NestedInteger())
            else:
                if s[i - 1].isdigit():
                    stack[-1].add(NestedInteger(num * sign))
                    num, sign = 0, 1
                if s[i] == ']':
                    top = stack.pop()
                    if stack:
                        stack[-1].add(top)
                    else:
                        return top
        