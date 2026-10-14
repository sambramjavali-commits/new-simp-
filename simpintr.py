import sys
def simple_intrest(principal,intrest,time):
    return (principal*intrest*time)/100

if __name__ == "__main__":
    p = float(sys.argv[1])
    i = float(sys.argv[2])
    t = float(sys.argv[3])


    
    print("Simple intrest is:",simple_intrest(p,i,t))