import numpy as np
import matplotlib.pyplot as plt


def get_finDiff_matrices(n):
    d1 = np.zeros((n, n))
    d2 = np.zeros((n, n))
    for i in range(1, n-1):
        d2[i, i-1] = 1
        d2[i, i] = -2
        d2[i, i+1] = 1
        #d1:
        d1[i, i-1] = 1
        d1[i, i+1] = -1
    
    return d1, d2

H = 1
y = np.linspace(0, H, num=n)

uthing = -0.5 * y**2 - H * 0.5 * y

def Carreau_Yasuda(uprev, eps, eta0=2, eta_inf=1, llambda=1, n=50, a=1, N=2, alpha = 0.5):
    
    Result = np.ones(n)
    Result[0] = 0
    Result[n-1] = 0
    d1, d2 = get_finDiff_matrices(n)

    diff = eps+1
    while diff > eps:
        #Get eta, calculate the derivative and set the values along the diagonal
        eta = eta_inf + (eta0 - eta_inf) * (1 + (llambda * uprev)**a)**((N-1)/a)
        etamat = np.diag(eta)
        deta = np.matmul(d1, eta)
        detamat = np.diag(deta)
        
        #The two halves of the matrix we get
        B = np.matmul(detamat, d1)
        A = np.matmul(etamat, d2)
        
        #Actually make the matrix
        Mat = A + B
        Mat[0,0] = 1
        Mat[n-1,n-1] = 1

        #Find our uhat
        uhat=np.linalg.solve(Mat, Result)
        
        unew = alpha * uprev + (1-alpha) * uhat
        diff = np.linalg.norm(unew - uprev)
        uprev = unew

    return unew

U = Carreau_Yasuda(uprev = uthing, eps=1e-5, alpha = 0.9)

plt.plot(y, U,'r-',linewidth=2,label='u')
plt.xlabel('Y')
plt.ylabel('Velocity')
plt.show()