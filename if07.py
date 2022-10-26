def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    d=0
    if a>0 and a%2==1:
        d="positive odd number"
    if a>0 and a%2==0:
        d="positive even number"
    if a<0 and a%2==1:
        d="negative odd number"
    if a<0 and a%2==0:
        d= "negative even number"
    if a==0:
        d="the number is zero"

    return d
print(main(-24))