import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    i=0
    a=[]
    while i<n:
        a=a+[i]
        i+=1
    return a 
