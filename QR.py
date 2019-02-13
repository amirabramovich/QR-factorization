#!/usr/bin/env python
import numpy as np


def qr(A):
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    A=np.transpose(A)
    R[0][0]=np.linalg.norm(A[0], 2)
    Q[:,0]=A[0]/R[0][0]
    for i in range(1,n):
        Q[:,i]=A[i]
        for j in range(0,i):
            R[j][i]=np.matmul(Q[:,j], Q[:,i])
            Q[:,i]=Q[:,i]-(R[j][i] * Q[:,j])
        R[i][i]=np.linalg.norm(Q[:,i], 2)
        Q[:,i]=Q[:,i]/R[i][i]
    return Q, R


def main():
    a = np.array([[2.0, 1.0, 2.0],
                  [1.0, -2.0, 1.0],
                  [1.0, 2.0, 3.0],
                  [1.0, 1.0, 1.0]])
    q, r = qr(a)
    print('Q:\n', q)
    print('R:\n', r)


if __name__ == '__main__':
    main()

