I = io.imread("cameraman.png")

J = np.zeros((h,w))
for i in np.arange(0,h,1):
  for j in np.arange(0,w,1):
    ind = I[i,j]
    J[i,j] = np.floor((255.0/(h*w))*H[ind]+0.5)

%matplotlib inline
fig=plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(I, cmap='gray')
plt.title("Cameraman image")

plt.subplot(1,2,2)
plt.imshow(J, cmap='gray')
plt.title("Cameraman after histogram equalization")
plt.show()
