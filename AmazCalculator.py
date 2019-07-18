# Amazing calculator. By: Ryandw11.

def pemdas(arr):
    ar = []
    for c in arr:
        ar.append(c)
    i = 0
    done = False
    while not done:
        if i >= len(ar) - 1:
            done = True
            break
        i = 0
        for c in ar:
            if c == "*":
                out = float(ar[i - 1]) * float(ar[i + 1])
                ar[i] = str(out)
                del ar[i - 1]
                del ar[i]
                break
            if c == "/":
                out = float(ar[i-1]) / float(ar[i+1])
                ar[i] = str(out)
                del ar[i - 1]
                del ar[i]
            i += 1
    return ar


def parse(input):
    ar = input.split(" ");
    ar = pemdas(ar)
    output = 0.0
    tempnum = ""
    tempop = ""
    for c in ar:
        if c == "+":
            tempop = "+"
        elif c == "-":
            tempop = "-"
        elif c == "*":
            tempop = "*"
        elif c == "/":
            tempop = "/"
        else:
            tempnum = c
            if output == 0.0:
                output = float(c)
            else:
                if (tempop == "+"):
                    output += float(tempnum)
                if (tempop == "-"):
                    output -= float(tempnum)
                if (tempop == "*"):
                    output *= float(tempnum)
                if (tempop == "/"):
                    try:
                        output /= float(tempnum)
                    except:
                        print("Error: Can not divide by zero!")
    return output

print("Welcome to the amazing calculator!")
print("Note: All statements must have spaces between the operation. Order of operations is not follower")
print("Example: 3 + 5 / 6")
# print(parse("3 / 0"))
while True:
    a = input("Please input in da math \n")
    if (a == "exit") | (a == "quit"):
        print("Thank you for using my amazing calculator.")
        break;
    else:
        print(parse(a))
