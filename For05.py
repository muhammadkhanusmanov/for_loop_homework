def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=[]
    while A<=B:
       a+=[B]
       B-=1 
    return a