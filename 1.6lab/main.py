if __name__ == "__main__":
    def i (s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s
    v1="abcd"
    v2="kolos"
    r1=i(v1)
    r2=i(v2)
    print(r1)
    print(r2)
