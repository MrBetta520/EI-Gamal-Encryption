import random

from params import p
from params import g

def keygen():
    q = (p - 1) // 2
    sk = random.randint(1, q)
    pk = pow(g, sk, p)
    return pk,sk


def encrypt(pk,m):
    q = (p - 1) // 2
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    c2 = (pow(pk, r, p) * m) % p
    return [c1,c2]


def decrypt(sk,c):
    c1, c2 = c
    c1_to_a = pow(c1, sk, p)
    c1_to_a_inv = modular_inverse(c1_to_a, p)
    m = (c2 * c1_to_a_inv) % p
    return m


def modular_inverse(a, m):
    """
    Calculates the modular inverse of 'a' modulo 'm'.
    There is no need to update this function.
    """
    return pow(a, -1, m)

