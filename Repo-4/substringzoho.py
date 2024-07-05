def isSubstring(s1, s2):
    M = len(s1)
    N = len(s2)


    for i in range(N - M + 1):




        for j in range(M):
            if (s2[i + j] != s1[j]):
                break

        if j + 1 == M:
            return i

    return -1




if __name__ == "__main__":
    s1 = "test123string"
    s2 = "123"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not Present")
    else:
        print("Present at index " + str(res))
