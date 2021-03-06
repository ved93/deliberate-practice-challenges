import random

def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j
   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1
      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 
      i += 1   
   return j, t

# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

if __name__ == '__main__':
   #  n = int(input())
   #  a = [int(x) for x in input().split()][:n]
   n = 5
   a = [2,3,9,1,2]

   randomized_quick_sort(a, 0, n - 1)
   for x in a:
      print(x, end=' ')
