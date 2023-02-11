"Module level docstring for hello.py"


def hello_world():
    """here we say hello"""
    print("hello, world")


def hello_world2(x: int) -> int:
    """here we say hello and process an integer
    
    Args:
        x (int): some integer argument
    """
    print("hello, world")

    return x**2 + 5