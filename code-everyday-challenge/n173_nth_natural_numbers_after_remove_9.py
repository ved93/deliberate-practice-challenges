
def findNthNumber(N):
       
    # Stores the Nth number
    result = 0
    p = 1
 
    # Iterate while N is
    # greater than 0
    while (N > 0):
       
        # Update result
        result += (p * (N % 9))
 
        # Divide N by 9
        N = N // 9
 
        # Multiply p by 10
        p = p * 10
    # Return result
    return result




if __name__ == '__main__':
    N = 82
    print(findNthNumber(N))