def generate_password(upper=2, lower=3, digit = 3, symbol = 2, repeat = True):
    if repeat:
        f = lambda x,y: random.choices(x,k=y)
    else:
        f = lambda x,y: random.sample(x,k=y)
    
    space = f(string.ascii_uppercase, upper)
    space.extend(f(string.ascii_lowercase, lower))
    space.extend(f(string.digits, digit))
    space.extend(f(string.punctuation, symbol))
    
    random.shuffle(space)
    
    return ''.join(space)


if __name__ == '__main__':
    
    import string
    import random

    for i in range(1):
        print('\n', generate_password(3,3,3,1,1))
