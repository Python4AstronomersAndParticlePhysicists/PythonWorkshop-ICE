import numpy as np

n = 100000
h0 = np.random.normal(57.74, 0.47, n)
distance = np.random.normal(500, 100, n)

velocity = np.mean(h0 * distance)
velocity_unc = np.std(h0 * distance)

print('({:.0f} ± {:.0f}) km/s'.format(velocity, velocity_unc))
