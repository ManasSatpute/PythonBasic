class Test:
    def __init__(self):
        print('Object Constructed')

    def __del__(self):
        print('Object Destructed')


t=Test()
del t
