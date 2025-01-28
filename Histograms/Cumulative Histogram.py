I = io.imread("cameraman.png")

#To compute histogram of image
h,w = I.shape
hist = np.zeros(256) #n_bins -256
for i in np.arange(0,h,1):
  for j in np.arange(0,w,1):
    hist[I[i,j]] += 1

%matplotlib inline
fig=plt.figure()
plt.plot(hist)
plt.title("Histogram of Cameraman")
plt.show()

#To compute cumulative histogram
H = np.zeros(256)
H[0] = hist[0]
for n in np.arange(1,256,1):
  H[n] = H[n-1] + hist[n]  #Adding present value to value occuring before

%matplotlib inline
fig=plt.figure()
plt.plot(H)
plt.title("Cumulative histogram of Cameraman")
plt.show()
