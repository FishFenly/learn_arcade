## p1
# for i in range(10):
#     print("*", end=" ")
# print("")

## p2
# for i in range(10):
#     print("*", end=" ")
# print("")
# for i in range(5):
#     print("*", end=" ")
# print("")
# for i in range(20):
#     print("*", end=" ")
# print("")

## p3
# for i in range(10):
#     for i in range(10):
#         print("*", end=" ")
#     print("")

## p8
# for x in range(10):
#     for i in range(x+1):
#         print(i, end=" ")
#     print()

## p9

# for x in range(10):
#     for y in range(x):
#         print(" ", end=" ")
#     for i in range(10-x):
#         print(i, end=" ")
#     print()

## p10

# for x in range(1,10):
#     for i in range(1,10):
#         print(x*i, end=" ")
#         if(x*i < 10):
#             print(" ", end="")
#     print()
# print()

## p11

# for x in range(10):
#     for z in range(10,x,-1):
#         print(" ", end=" ")
#     for i in range(x):
#         print(i+1, end=" ")
#     for y in range(x-1,0,-1):
#         print(y, end=" ")
#     print()

## problem12

for x in range(10):
    for z in range(10,x,-1):
        print(" ", end=" ")
    for i in range(x):
        print(i+1, end=" ")
    for y in range(x-1,0,-1):
        print(y, end=" ")
    print()
for x in range(10):
    for y in range(x+2):
        print(" ", end=" ")
    for i in range(8-x):
        print(i+1, end=" ")
    for z in range(7-x,0,-1):
           print(z, end=" ")
    print()