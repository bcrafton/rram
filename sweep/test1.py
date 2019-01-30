
import numpy as np
np.set_printoptions(threshold=np.inf)

gap_min = np.linspace(-11., -10., 10)
gap_min = np.power(10., gap_min)
gap_min = gap_min.tolist()
gap_min = [1e-11, 2e-11, 3e-11, 4e-11, 5e-11, 6e-11, 7e-11, 8e-11, 9e-11, 10e-11]

gap_max = np.linspace(-10., -8., 10)
gap_max = np.power(10., gap_max)
gap_max = gap_max.tolist()
gap_max = [1e-10, 2e-10, 3e-10, 4e-10, 5e-10, 6e-10, 7e-10, 8e-10, 9e-10, 10e-10]

I0 = np.linspace(-8., -3., 10)
I0 = np.power(10., I0)
I0 = I0.tolist()

g0 = np.linspace(-11., -7., 10)
g0 = np.power(10., g0)
g0 = g0.tolist()

results = []
for _gap_min in gap_min:
    for _gap_max in gap_max:
        for _I0 in I0:
            for _g0 in g0:
                if _gap_max > _gap_min:
                    Rmin = 1. / (_I0 * np.exp(-_gap_min / _g0))
                    Rmax = 1. / (_I0 * np.exp(-_gap_max / _g0))

                    # print (Rmin, Rmax)

                    if np.isnan(Rmin) or np.isnan(Rmax) or np.isinf(Rmin) or np.isinf(Rmax):
                        continue

                    results.append((_gap_min, _gap_max, _I0, _g0, Rmin, Rmax, Rmax / Rmin))


results = np.array(results)

idx1 = np.where( (results[:, 4] > 5e5) * (results[:, 4] < 5e6) )
idx2 = np.where( (results[:, 5] > 5e7) * (results[:, 5] < 5e8) )
idx3 = np.where( (results[:, 6] > 90.) * (results[:, 6] < 150.) )

idx = np.intersect1d(idx1, idx2)
idx = np.intersect1d(idx, idx3)

print (idx)
print (results[idx][:, 0:4])
print (results[idx][:, 4:7])
