def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    i=1
    s=0
    while i<=N:
        s+=1/i
        i+=1
    return s