

def regla_d_tres_simple(n1,d1,n2,d2):
    if n1 == 0:
        n1 = (d1 * n2) / d2
        return n1
    elif d1 == 0:
        d1 = (n1 * d2) / n2
        return d1
    elif n2 == 0:
        n2 = (n1 * d2) / d1
        return n2
    elif d2 == 0:
        d2 = (d1 * n2) / n1
        return d2
    else:
        return "Error: Solo uno valor puede ser cero."

if __name__ == "__main__":
    print(regla_d_tres_simple(1, 2, 0, 16))