from collections import deque

## Create a buffer to hold the key chain lines
buffer = deque('a', 23)

def extractAccountAndPassword():
    account="Error: No Account Found"
    password="Error: No Password Found"

    for index, item in enumerate(buffer):
        if "acct" in item:
            account=item.replace('"', '').replace('acct<blob>=', '')

        if "data:" == item:
            password = buffer[index+1].strip('"')
    print("%s\t%s" % (account, password))


def checkBuffer():
    isWifi = False;

    for item in buffer:
        if "AirPort network password" in item:
            isWifi = True;
    
    if isWifi:  
        extractAccountAndPassword()
       

def main():
    with open('keychain_all.txt', 'r') as inf:
        for line in inf:
            line = line.strip()
            buffer.append(line)
            
            if "keychain:" in line:
               checkBuffer()

    checkBuffer() # Check one last time
 

if __name__ == '__main__':
   main()
