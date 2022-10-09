# def remove_duplicate(L):
#     boundary = 0
#     counter = 0
#     for i in range(len(L)):
#         if(len(L) == 0):
#             return 0
#         if(len(L) == 1):
#             return 1
#         if(L[i-1] != L[i]):
#             counter += 1
#             L[boundary] = L[i]
#             boundary += 1            
            
#     return counter,L

# print(remove_duplicate([1,2]))


def runningSum(L):
    for i in range(len(L)):
        if(i != 0):
            L[i] = L[i-1] + L[i]
    return L

# print(runningSum([1,1,1,1,1]))


def pivotIndex(L):
    sum = 0
    sum2 = 0
    for numb in L:
        sum += numb
    for i in range(len(L)):
        sum2 += L[i]
        if(sum - sum2 - L[i] == sum):
            return i
    return -1

# print(pivotIndex([1,7,6,5,6]))


def isIsomorphic(s, t):
    counterT = 0
    counterS = 0
    counter = 0
    length_s = len(s)
    length_t = len(t)
    if(length_s != length_t):
        return False
    for i in range(length_s):
        for j in range(length_s):
            if(s[j] == s[i]):
                counterS +=1
            if(t[j] == t[i]):
                counterT +=1
            if(t[j] == t[i] and s[j] == s[i]):
                counter +=1

    if(counter != counterT or counter != counterS):
        return False
    return True


# print(isIsomorphic("bbbaaaba","aaabbbba"))


def isSubsequence(s,t):
    string_list = [x for x in s]
    new_string = ""
    counter = 0
    for i in range(len(t)):
        if(t[i] in string_list and s[counter] == t[i]):
            new_string += t[i]
            counter += 1
    if(new_string == s):
        return True
    return False

# print(isSubsequence("ab","baab"))


def isIsomorphic(s,t):
        
    mapping_s_t = {}
    mapping_t_s = {}
        
    for c1, c2 in zip(s, t):
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
            
    return True

# print(isIsomorphic("bbbaaaba","aaabbbba"))

def findSubstring(s, words):
    list_of_subs = []
    list_of_s = []
    list_of_indexes = []
    perms = list(itertools.permutations(words))
    
    for permutation in perms:
        list_of_subs.append(''.join(permutation))

    counter2 = len(words[0]) * len(words)
    p = 0
    while (p < len(s)):
        list_of_s.append(s[p:counter2])
        if(list_of_s[p] in list_of_subs):
            list_of_indexes.append(p)
        counter2+=1
        p +=1
    
    return list_of_indexes, list_of_subs,list_of_s
    
# print(findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#             self.val = val
#             self.next = next
# class Solution(object):    
#     def mergeTwoLists(self, list1, list2):
#         current = ListNode(0)
#         while(list1 != None and list2 != None):
#             if(list1.val < list2.val):
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
        
#         return current.next

# temp = Solution()
# print(temp.mergeTwoLists([1,2,4],[1,3,4]))


# def twoSum(L, target):
#     new_list = []
#     for i in range(len(L)):
#         for j in range(i+1,len(L)):
#             if(L[i] + L[j] == target):
#                 new_list.append(i)
#                 new_list.append(j)
#                 return new_list
#     return []


# print(twoSum([3,2,4],6))

# def longestCommonPrefix(strs):
#         new_list = []
#         for i in range(len(strs[0])):
#             new_list.append(strs[0][i])
            
#         for j in range(len(strs)):
#             new_str = ""
#             counter = 0
#             for k in range(len(strs[j])):
#                 if(strs[j][k] == new_list[counter]):
#                     counter += 1
#                     new_str += strs[j][k]
#                 if(k == len(strs[j])-1 and counter <= 1 and len(strs[0]) != 1):
#                     return ""
            
#         return new_str
    
    
# print(longestCommonPrefix(["lower","jbaaa"]))


def isPowerOfTwo(n):
        if(n == 1):
            return True
        else:
            num = 2
            while(True):
                num *= 2
                if(num == n):
                    return True
                elif(num > n):
                    return False
        
# print(isPowerOfTwo(16))


def removeDuplicates(nums):
        table = {}
        removed = 0
        i = 0
        while(i < len(nums)):
            if(nums[i] not in table):
                table[nums[i]] = i
                i +=1
            else:
                removed +=1
                counter = i
                while(counter < len(nums)-1):
                    temp = nums[counter+1]
                    nums[counter+1] = nums[counter]
                    nums[counter] = temp
                    counter += 1
        final_length = len(nums) - removed
            
        return final_length,nums,table
    
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



def longestPalindrome(s):
    index2 = len(s)-1
    index1 = 0
    single_letter = ""
    string_left = ""
    string_right = ""
    length_ind = len(s)//2
    if(len(s) == 1):
        return s[0]
    for i in range(length_ind):
        if(len(s) % 2 == 1):
            single_letter = s[length_ind]
        if(s[index2] == s[index1]):
            string_left += s[index1]
            string_right += s[index2]
        if(s[index2] != s[index1]):
            string_left = ""
            string_right = ""
        index1 += 1
        index2 -=1
    final_string = string_left + single_letter + string_right[::-1]

    return final_string


# print(longestPalindrome("bb"))

def lengthOfLongestSubstring(s):
    diction = {}
    dict_solution = {}
    count = 0
    strs = ""
    for c in s:
        if(c not in diction):
            diction[c] = c
            strs += c
            count += 1
        else:
            dict_solution[strs] = count
            diction.clear()
            count = 1
            strs = f'{c}'
            print(strs,count)
            
    return max(dict_solution, key=dict_solution.get),dict_solution


# print(lengthOfLongestSubstring("pwwkew"))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        diction = {}
        curr = head
        
        while(curr is not None):
            if(curr in diction): return curr
            diction[curr] = 0
            curr = curr.next
        return -1
    
    
# temp = Solution()
# temp.detectCycle([3,2,0,-4])

# def minCap(L,cap):
#     mini = L[0]
#     for i in range(0,cap+1):
#         if(L[i] < mini):
#             mini = L[i]
            
#     return mini


# def maxProfit(prices):
#     res = 0
#     right = len(prices)-1
#     len_prices = len(prices)
    
#     if(len_prices == 1 or len_prices == 0):
#         return 0
    
#     while(right > 0):
#         minimum_left = minCap(prices,right-1)
#         addition = prices[right] - minimum_left
#         if(prices[-1] < minimum_left):
#             return 0
#         if(addition > res and addition > 0):
#             res = addition
#         right -= 1
    
#     return res

# print(maxProfit([2,1,4]))

def longestPalindrome(s):
    diction = {}
    sum = 0
    unpaired = False
        
    for i in range(len(s)):
        if(s[i] not in diction):
            diction[s[i]] = 1
        else:
            diction[s[i]] += 1
            
    for key in diction:
        if(diction[key] % 2 == 0):
            sum += diction[key]
        else:
            sum += diction[key] - 1
            unpaired = True 

    print(diction)
    if(unpaired):
        return sum + 1
    return sum


# print(longestPalindrome("bananas")) 


def maxProfit(prices):
    left = 0
    right = 1
    
    max_profit = 0
    
    for i in range(len(prices)):
        addition = prices[right] - prices[left]
        if(addition > max_profit):
            max_profit = addition
            right += 1
        else:
            left = right
            right += 1
    
    return max_profit
