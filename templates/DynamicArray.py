# import ctypes

# class DynamicArray(object):

#     def __init__(self):

#         self.n = 0
#         self.capacity = 1
#         self.A = self.make_array(self.capacity)

# # method that returns the length of the list
#     def __len__(self):
#         return self.n

# # method for indexing the list
#     def __getitem__(self, k):
#         if not 0<= k < self.n:
#             return IndexError('k is out of bounds')
#         return self.A[k] 

# # method for appending an element
#     def append(self, ele):
#         if self.n == self.capacity:
#             self._resize(2*self.capacity) #2x if capacity is not enough

#         self.A[self.n] = ele  #insert the new element at the end of the list
#         self.n += 1   # increase the length of the list
    
#     def _resize(self, new_cap):
#         B = self.make_array(new_cap) #making a new bigger array
#         for k in range(self.n):
#             B[k] = self.A[k]  #referencing the existing values from A into B
#         self.A = B
#         self.capacity = new_cap

# # a method that makes the array itself
#     def make_array(self, new_cap):
#         return (new_cap * ctypes.py_object)()


# arr = DynamicArray()

# arr.append(1)
# print(len(arr))
# print(arr[0])


# # When a dynamic array gets full it doubles in size

# # ###### Array Exercise  ##################

# # Anagram Check - Given two strings check if they are anagrams, ignore sapce and capitalisation 

# def anagramCheck(first_str, sec_str):
#     first_str = list(first_str.lower().replace(' ',''))
#     sec_str = list(sec_str.lower().replace(' ',''))

#     first_str = sorted(first_str)
#     sec_str = sorted(sec_str)
#     if first_str == sec_str:
#         return True 
#     else:
#         return False

# print(anagramCheck('go go go ', 'gggooo'))
# print(anagramCheck('abc ', 'cba'))
# print(anagramCheck('hi man ', 'hi   man'))
# print(anagramCheck('123 ', '1  2'))


# # #### Array pair sum #######
# # Given an integer array, output all the unique pairs that sum up to a specific value k

# pairs=[]
# def pairSum(arr, num):
#     for n in arr:
#         for i in range(len(arr)):
#             if n + arr[i] == num:
#                 pair = (n, arr[i])
#                 pair = sorted(list(pair))
#                 if pair not in pairs:
#                     pairs.append(pair)
#                     # print(tuple(pair))
#     print(pairs)
#     return len(pairs)                
                 
# # print(pairSum([1, 2, 3, 1], 3))
# # pairSum([1, 3, 2, 2], 4)
# # print(pairSum([1,9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))

# def pair_sum(arr, num):
#      seen = set()
#      output = set()

#      for k in arr:
#          target = num - k
#          if target not in seen:
#              seen.add(k)
#          else:
#              output.add((min(k, target), max(k, target)))
#      print(seen)
#      return (output, len(output))

# print(pair_sum([1,9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))


# ################### Find the Missing Element ############################

# # Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array

# def ele_finder(arr1, arr2):
#     fig = set()
#     for num in arr1:
#         if arr1.count(num) != arr2.count(num):
#             fig.add(num)
#     print(str(fig.pop()) + ' is the missing number')


# ele_finder([5, 5, 7, 7], [5, 7, 7])
# ele_finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])

# # using exclusive or XOR '^'
# def finder(arr1, arr2):
#     result = 0

#     for num in arr1+arr2:
#         result ^= num
#         print(result)

# finder([5, 5, 7, 7], [5, 7, 7])

################# Largest Continuous Sum ##############################
# def contSum(arr):
#     num_sum = 0
#     max_num = []

#     if len(arr) == 0:
#         return 0

#     for num in arr:
#         num_sum += num
#         max_num.append(num_sum)
    
#     return max(max_num)

# print(contSum([1, 2, -1, 3, 4, -1]))
# print(contSum([1, 2, -1, 3, 4, 10, 10, -10, -1]))


################# String Reversal #################################
# def strReverse(strn):
#     strin = strn.split()
#     strin.reverse()
#     reversedstr = ' '.join(strin)
#     return reversedstr


# print(strReverse('   space before'))
# print(strReverse('space after    '))
# print(strReverse('   Hello John  how are you  '))


#################### String Compression ###############################
# def strCompress(s):
#     com = set(s)
#     compressed = ''
    
#     for letter in com:
#         num = s.count(letter)
#         compressed += (letter + str(num))

#     return compressed

# print(strCompress(''))
# print(strCompress('AABBCC'))
# print(strCompress('AAABCCDDDDD'))

################## Unique Characters in a String ########################
# Given a string, all the characters in the string must be unique as in 'abcd' no doubles. if so, return true, otherwise return false

def uniqueChr(s):
    
    # if s == '':
    #     return True

    rec = []
    for char in s:
        rec.append(s.count(char))

    if sum(rec) > len(s):
        return False
    elif sum(rec) == len(s):
        return True
       

print(uniqueChr(''))
print(uniqueChr('goo'))
print(uniqueChr('abcdesfg'))

