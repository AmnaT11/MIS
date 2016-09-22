def move(n, source, bridge, destination):
    if n==1:
        print('%s --> %s' % (source, destination))
    else:
        move(n-1, source, destination, bridge)
        print('%s --> %s' % (source, destination))
        move(n-1, bridge, source, destination)

    move(3, 'A', 'B', 'C')

    input()