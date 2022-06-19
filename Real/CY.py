import numpy as np

#def Carreau-Yasuda(eta0=2, eta_inf=1, llambda=1, u0, n=1, a=1):
n = 3
H = 2
y = np.linspace(0, H, num=n)
eta0=2
eta_inf=1
llambda=1
#u0 = Some function of y
N=1
a=1

eta = y**2
#eta = eta_inf + (eta0 - eta_inf) * (1 + (llambda * u0)**a)**((n-1)/2)

d1 = np.zeros((n, n))
d2 = np.zeros((n, n))
for i in range(1, n-1):
    d2[i, i-1] = 1
    d2[i, i] = -2
    d2[i, i+1] = 1
    #d1:
    d1[i, i-1] = -1
    d1[i, i+1] = 1

etamat = np.diag(eta)
deta = np.matmul(d1, eta)
detamat = np.diag(deta)

B = np.matmul(detamat, d1)
A = np.matmul(etamat, d2)

Mat = A + B
Mat[0,0] = 1
Mat[2,2] = 1

Result = np.array([0,1,0])

u=np.linalg.solve(Mat, Result)
print(u)