def move(N, FROM, TO, SPARE):
    """
    recursive way

    Parameters
    ----------
    N : int
        sum of disk
    FROM : string or something
        first tower
    TO : string or something
        end tower
    SPARE : string or something
        spare tower
    """
    if(N == 0):
        print("done")
    else:
        move(N-1, FROM, SPARE, TO)
        print("move {:d} {:s} {:s}".format(N, FROM, TO))
        move(N-1, SPARE, TO, FROM)


def imove(N, FROM, TO, SPARE):
    """
    iterative way

    Parameters
    ----------
    N : int
        sum of disk
    FROM : string or something
        first tower
    TO : string or something
        end tower
    SPARE : string or something
        spare tower
    """
    if(N == 0):
        print("done")
    else:
        imove(N-1,)


move(4, "FROM", "TO", "SPARE")
