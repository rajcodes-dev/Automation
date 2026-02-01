import sys, openpyxl

if len(sys.argv) != 4:
    print("enter min. 4 arguments")
    sys.exit()
N = int(sys.argv[1])
M = int(sys.argv[2])
file_name = sys.argv[3]


