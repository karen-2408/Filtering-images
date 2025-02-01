I = io.imread("cameraman.png")

H = np.zeros(256)
H[0] = hist[0]
for n in np.arange(1,256,1):
  H[n] = H[n-1] + hist[n]

K = np.zeros((h,w))
for i in np.arange(0,h,1):
  for j in np.arange(0,w,1):
    pa = H[I[i,j]]/(h*w) 
    K[i,j] = np.searchsorted(refH,pa) 

%matplotlib inline
fig=plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(I, cmap='gray')
plt.title("Cameraman image")

plt.subplot(1,2,2)
plt.imshow(K, cmap='gray')
plt.title("Cameraman after histogram shaping")
plt.show()
