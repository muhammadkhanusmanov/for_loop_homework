def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s=0
    i=1
    while i<N:
        s+=i
        i+=2
    return s