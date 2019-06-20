#Murad Ali, alixx800, Lab Section 008, Homework 3 Problem A

def main():
    R = int(input("Red component: "))
    G = int(input("Green component: "))
    B = int(input("Blue component: "))
    CMYK = RBG_to_CMYK(R, G, B)
    print ("CMYK representation: ", CMYK[0], CMYK[1], CMYK[2], CMYK[3])

def RBG_to_CMYK(R, G, B):
    R_prime = R / 255
    G_prime = G / 255
    B_prime = B / 255
    if (R_prime == 0) and (G_prime == 0) and (B_prime == 0):
        return [0, 0, 0, 100]
    else:
        K = 1 - max(R_prime, G_prime, B_prime)
        C = 100 * (1 - R_prime - K)/(1 - K)
        M = 100 * (1 - G_prime - K)/(1 - K)
        Y = 100 * (1 - B_prime - K)/(1 - K)
        K = round (100 * K)
        return([int(C + .5), int(M + .5), int(Y + .5), int(K + .5)])


if __name__ == "__main__":
    main()
