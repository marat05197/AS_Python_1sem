def RemoveCols(A, K1, K2):
    M = len(A)
    if M == 0:
        return A
    
    N = len(A[0])
    if K1 > N:
        return A
    
    start = K1 - 1
    end = min(K2, N)
    
    for i in range(M):
        A[i] = A[i][:start] + A[i][end:]
    
    return A
