#User function Template for python3

class Solution:
    def rotate(self, arr):
        last =arr.pop()
        arr.insert(0,last)
        
        return arr
