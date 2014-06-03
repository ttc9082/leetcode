
class Solution:
    def reverseWords(self, s):
        l = s.split()
        l.reverse()
        return " ".join(l)

    def reverseWords2(self, s):
        return " ".join(s.split()[::-1])

    def reverseWords3(self, s):
        word_list = s.split(' ')
        if len(word_list) == 0:
            return ""
        new_list = []
        for i in xrange(len(word_list)):
            if word_list[-i-1] != "":
                new_list.append(word_list[-i-1])
        return ' '.join(new_list)
str = 'TTc loves YH'
print Solution().reverseWords(str)
print Solution().reverseWords2(str)
print Solution().reverseWords3(str)
