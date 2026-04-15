from sys import argv
from Chudnovsky.chudnovsky import chudnovsky

methods = {"Chudnovsky":chudnovsky}

if __name__ == '__main__':
    '''if len(argv)!=2:
        print("[-] Invalid arguments detected")'''
    # TODO: Command line arguments

    print("[+] Listing pi algorithms...\n")

    i = 0
    for method,func in methods.items():
        print(f"({i}) {method}")
    
    user = int(input("\n[X] Choose an option (number):"))

    if not(0<=user<=i):
        print("Invalid input, exiting...")
        exit()

    i=0
    for method,func in methods.items():
        if i==user:
            user1 = int(input("Enter number of digits to calculate:"))
            
            print() # Some space
            
            # Call the function associated with that algorithm
            print(func(user1)) # TODO: replace with file output
            break
        i+=1
