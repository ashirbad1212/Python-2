#Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.

def evenodd(N):
    evenlist = []
    oddlist = []
    for i in N:
        if (i % 2 == 0):          #finding even values and putting it in even list
            evenlist.append(i)
        else:
            oddlist.append(i)      #putting odd values in another list
    print("Even lists are:", evenlist)
    print("Odd lists are:", oddlist)


N = list()
n = int(input("Enter the size of  List 1 ::"))
print("Enter the Elements of  List 1::")
for i in range(int(n)):
    k = int(input(""))
    N.append(k)
evenodd(N)