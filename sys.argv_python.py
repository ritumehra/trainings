import sys

USAGE = '''
1. TEST_USAGE_1
2. TEST_USAGE_2
3. TEST_USAGE_3
4. TEST_USAGE_4
'''

print("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))

try:
    if len(sys.argv) <= 1:
        sys.exit()
    else:
        mode = sys.argv[1]
        print(mode)
except:
    print ('')
    print(sys.stderr, USAGE)
    sys.exit()
