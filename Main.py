
def Display(iNo):

    if iNo < 0:
        iNo = -iNo

    for x in range(1,iNo+1):
        print("#\t",x,"\t*",end="\t")
    
    print()

def main():

    iValue = int(input("Enter Number\n"))
    Display(iValue)

if __name__ == "__main__":
    main()