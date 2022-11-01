def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=[]
    while A<=B:
       a+=[A]
       A+=1 
    return a 
