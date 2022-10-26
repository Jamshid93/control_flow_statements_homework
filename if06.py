def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    d
    if a>0 and b>0 and c>0:
        d="there are a lot of positive numbers"
    if a>0 and b>0 and c<0:
        d="there are a lot of positive numbers"
    if a>0 and b<0 and c>0:
        d="there are a lot of positive numbers"
    if a<0 and b>0 and c>0:
        d="there are a lot of positive numbers"
    else:
        d="there are a lot of negative numbers"
    return d
print(main(-2,4,1))