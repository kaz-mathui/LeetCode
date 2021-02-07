
pre_idx = 0

def test():
    for i in range(1, 4):
        for j in range(i-1, -1, -1):
            print(j)

if __name__ == '__main__':
    print(test())