import math


#bubble sort

def bubbleSort(list):
    for i in range(len(list)):
        for j in range(1,len(list)):
            if(list[j - 1] > list[j]):
                temp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = temp
    return list

# print(bubbleSort([4,1,5,6,2,4,6]))


#min in list from chosen index

def minStartFrom(index,list):
    minimum = list[0]
    for i in range(index,len(list) - 1):
        if(list[i] < minimum):
            minimum = list[i]
    return minimum

# print(minStartFrom(0,[394,0,6,7,7,3,9,1,3]))


#selection sort

def selectionSort(list):
    for i in range(len(list) - 1):
        for j in range(i,len(list) - 1):
            if(list[j] < list[i]):
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    return list

# print(selectionSort([4,1,5,6,2,4,6]))


#insertion sort

def insertionSort(list):
    list_length = len(list)
    for i in range(list_length):
        count = i
        for j in range(i+1,list_length):
            if(list[j] < list[count]):
                while(list[j] < list[count]):
                    temp = list[j]
                    list[j] = list[count]
                    list[count] = temp
                    count -=1
    return list

# print(insertionSort([4,1,5,6,2,4,6]))


#min

def min(list):
    minimum = list[0]
    for i in range(len(list) - 1):
        if(list[i] < minimum):
            minimum = list[i]
    return minimum

# print(min(8,[394,0,6,7,7,3,9,1,3]))


#min in list from chosen index ending

def minEndAt(index,list):
    minimum = list[0]
    for i in range(0,index):
        if(list[i] < minimum):
            minimum = list[i]
    return minimum

# print(minEndAt(8,[394,1,6,7,7,3,9,0,3]))


#merge sort

def mergeSort(list):
    if(len(list) > 1):
        
        half_list = len(list) // 2
        list_left = list[:half_list]
        list_right = list[half_list:]
        
        mergeSort(list_left)
        mergeSort(list_right)
        
        i = 0
        j = 0
        k = 0
        
        while(i < len(list_left) and j < len(list_right)):
            if(list_left[i] > list_right[j]):
                list[k] = list_right[j]
                j += 1
            else:
                list[k] = list_left[i]
                i += 1
            k += 1
        
        while(i < len(list_left)):
            list[k] = list_left[i]
            i += 1
            k += 1
            
        while(j < len(list_right)):
            list[k] = list_right[j]
            j += 1
            k += 1
        
    return list


# print(mergeSort([394,1,6,7,7,3,9,0,3]))

# quick sort

def quickSort(l):
    #TODO
    
    #TODO
    
    pivot = l[len(l) - 1]
    boundary = 0
    for i in range(1,len(l) - 1):
        if(l[i] < pivot):
            temp = l[boundary]
            l[boundary] = l[i]
            l[i] = temp
            boundary += 1
        if(i == len(l) - 1 and l[boundary] > pivot):
            temp2 = l[boundary]
            l[boundary] = pivot
            pivot = temp2
            boundary += 1     
    return l


# print(quickSort([1,6,7,7,3,9,0,3]))


# get max int in list

def get_max(list):
    max = list[0]
    for i in range(len(list) - 1):
        if(list[i] > max):
            max = list[i]
    return max

# print(get_max([1,6,7,7,3,9,0,3]))


# counting sort

def countingSort(list):
    x = 0
    max_list = get_max(list)
    list_occurrences = [0] * (max_list + 1)
    for i in range(len(list)):
        list_occurrences[list[i]] += 1
    for j in range(len(list_occurrences)):
        count = 0
        if(list_occurrences[j] != 0):
            while(count < list_occurrences[j]):
                list[x] = j
                count += 1
                x += 1
    return list

# print(countingSort([1,6,7,7,3,9,0,3]))


# bucket sort

def bucketSort(list):
    #TODO
    pass


def linearSearch(L,val):
    for i in range(len(L) - 1):
        if(L[i] == val):
            return i
    return -1

# print(linearSearch([1,6,7,7,3,9,0,3],3))


# binary search iterative

def binarySearchIterative(L,val):
    L = mergeSort(L)
    i = 0
    j = len(L) - 1
    while (i <= j):
        middle = (i + j) // 2
        if(val == L[middle]):
            return middle
        elif(val > L[middle]):
            i = middle + 1
        else:
            j = middle - 1
    return -1
    
    
# print(binarySearchIterative([1,6,7,7,3,9,0,3],6))


# binary search recursive

def binarySearchRecursive(L,val,left,right):
    L = mergeSort(L)
    
    if(left > right):
        return -1
    else:
        middle = (left + right) // 2
        if(L[middle] == val):
            return middle
        elif(L[middle] > val):
            binarySearchRecursive(L,val,left,middle-1)
        else:   
            binarySearchRecursive(L,val,middle + 1,right)


def final_binary_search_recursive(L,val):
    binarySearchRecursive(L,val,0,len(L)-1)
    
    
def ternarySearchRecursive(L,val,left,right):
    L = mergeSort(L)
    
    if(left > right):
        return -1
    else:
        partition = (right - left) // 3
        mid1 = left + partition
        mid2 = right - partition
        if(L[mid1] == val):
            return mid1
        elif(L[mid2] == val):
            return mid2
        elif(val > L[mid1] and val < L[mid2]):
            ternarySearchRecursive(L,val,mid1 + 1,mid2 - 1)
        elif(val < L[mid1]):
            ternarySearchRecursive(L,val,left,mid1 -1)
        elif(val > L[mid2]):
            ternarySearchRecursive(L,val,mid2 + 1,right)
        
        
def final_ternary_search_recursive(L,val):
    ternarySearchRecursive(L,val,0,len(L)-1)

# String Manipulation

def vowelsInString(s):
    count = 0
    vowels = ['A','E','O','U','I']
    for i in range(len(vowels)):
        for j in range(len(s)):
            if(s[j].upper() == vowels[i]):
                count += 1
    return count


# print(vowelsInString("aeoui"))


def reverseString(s):
    return s[::-1]

def revString(s):
    new_str = ""
    i = len(s) - 1
    while(i >= 0):
        new_str += s[i]
        i -= 1
    return new_str

# print(revString("Bryan"))

def reverseWordOrder(s):  #TODO
    words = []
    word_string = ""
    final_word = ""
    for i in range(len(s)):
        word_string += s[i]
        if(s[i] == " "):
            words.append(word_string)
            word_string = ""
    j = len(words) - 1
    while(j >= 0):
        final_word += words[j] + " "
        j -= 1
    return final_word

# print(reverseWordOrder("Trees are Beautiful"))


def rotation(s,shift):
    i = len(s) - 1
    new_str = ""
    while(i >= (len(s)) - shift):
        new_str += s[i]
        i -= 1
    for j in range(len(s) - shift):
        new_str += s[j]
    return new_str

# print(rotation('Nfokho',4))

def duplicate0(s):
    new_str = ""
    hashSet = set()
    for ch in s:
        if(ch not in hashSet):
            hashSet.add(ch)
            new_str += ch
            
    return new_str

# print(duplicate0("Hellooo!!"))

def duplicate(s):  #TODO
    unwanted = []
    new_str = ""
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if(s[i] == s[j]):
                count += 1
            if(count > 1):
                unwanted.append(j)
    for x in range(len(s)):
        counter = 0
        for y in range(len(unwanted)):
            if(x == unwanted[y]):
                counter += 1
        if(counter == 0):
            new_str += s[x]
    print(unwanted)
    return new_str

# print(duplicate("Hellooo!!"))


def mostRepeated(s):
    maximum = 0
    index = 0
    s = s.lower()
    for i in range(len(s)):
        counter = 0
        for j in range(len(s)):
            if(s[j] == s[i]):
                counter += 1
        if(counter > maximum):
            maximum = counter
            index = s[i]
    return index

# print(mostRepeated('Hellooo!!'))


def capitalize(s):  #TODO
    final_str = ""
    words = []
    word_string = ""
    for i in range(len(s)):
        if(s[i] != " "):
            if(s[i - 1] == " " or i == 0):
                word_string += s[i].upper()
            else:
                word_string += s[i]
        if(s[i] == " " and s[i + 1] != " " and i != len(s)):
            words.append(word_string)
            word_string = ""
        print(words)
    for word in words:
        final_str += word + " "
    return final_str

# print(capitalize('     bas          wle eir'))

def anagram(s1,s2):  # doesn't work since we need to check several occurences
    if(len(s1) != len(s2)):
            return False
    else:
        hash_set = set()
        for ch in s1:
            hash_set.add(ch)
        for ch in s2:
            if(ch not in hash_set):
                return False
        return True
    
    
def anagram2(s1,s2):
    list1 = [ch.upper() for ch in s1]
    list2 = [char.upper() for char in s2]
    sort = bubbleSort(list2)
    return list1 == list2

# print(anagram2('abcd','cdab'))


def palindrome(s):
    middle = len(s) // 2
    i = 0
    j = len(s)-1
    while(i < middle and j >= middle):
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

# print(palindrome("abcba"))


def jumpSearch(L,val):
    L = mergeSort(L)
    block_size = math.ceil(math.sqrt(len(L)))
    start = 0
    end = block_size
    print(L)
    
    while(start <= len(L) and L[end - 1] < val):
        start = block_size
        end += block_size
        if(end > len(L)):
            end = len(L)
    if(L[end - 1] > val):
        for i in range(start,end):
            if(L[i] == val):
                return i
    return -1    
            
# print(jumpSearch([1,2,46,3,2,1,45,6,62,1,6],45))


def exponential_search(L,val):
    L = mergeSort(L)
    bound = 1
    while(L[bound] < val and bound < len(L)):
        bound *= 2
        if(bound > len(L)):
            bound = len(L)
    if(L[bound] == val):
        return bound
    elif(L[bound > val]):
        binary_search = binarySearchRecursive(L,val,bound//2,bound)
        return binary_search
    return -1


# print(exponential_search([1,2,46,3,2,1,45,6,62,1,6],45))