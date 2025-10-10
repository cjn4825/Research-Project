import matplotlib.pyplot as plt


figure = plt.figure(figsize=(14.44, 6.73))

xData = [1, 2, 3, 4, 5]
yData = [2, 4, 6, 8, 10]

plt.plot(xData, yData)
plt.xlabel("test X-axis")
plt.ylabel("test Y-axis")
plt.title("Test Graph")

plt.savefig("testGraph.png", dpi=300)
