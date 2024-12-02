loc = 10.0 #mean
scale = 3  #standard deviation
size = 100000

samples = np.random.normal(loc, scale, size)


# create a blank plot
fig, ax = plt.subplots(figsize = (12,5))

num_bins = 60

ax.set_title(f'Representation of 10^4 values with mean 10.0 and standard deviation of 3.0')

counts, bin_edges = np.histogram(samples, bins=num_bins)



plt.bar(bin_edges[:-1], counts / (size * np.diff(bin_edges)), width=np.diff(bin_edges), align='edge')

x = np.linspace(loc - 4*scale, loc + 4*scale, 1000)

#x = np.linspace(0,20,100001)

y = f(x, mu = loc, sigma = scale)


ax.plot(x,y);




