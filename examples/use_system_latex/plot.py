import matplotlib.pyplot as plt
import numpy as np


formula = (
    r'$\displaystyle '
    r'N = \int_{E_\text{min}}^{E_\text{max}} '
    r'\int_0^A'
    r'\int_{t_\text{min}}^{t_\text{max}} '
    r' Φ_0 \left(\frac{E}{\SI{1}{\GeV}}\right)^{\!\!-γ}'
    r' \, \symup{d}A \, \symup{d}t \, \symup{d}E'
    r'$'
)


def power_law_spectrum(energy, normalisation, spectral_index):
    return normalisation * energy**(-spectral_index)


bin_edges = np.logspace(2, 5, 15)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])


plt.errorbar(
    bin_centers,
    power_law_spectrum(bin_centers, 1e-12, 2.5),
    xerr=[bin_centers - bin_edges[:-1], bin_edges[1:] - bin_centers],
    yerr=0.2 * power_law_spectrum(bin_centers, 1e-12, 2.5),
    linestyle='',
)

plt.xlabel(r'$E \mathbin{/} \si{\giga\electronvolt}$')
plt.ylabel(
    r'$Φ'
    r'\mathbin{/}'
    r'\si{\per\GeV\per\second\per\steradian\per\meter\squared}$'
)

plt.text(0.1, 0.1, formula, transform=plt.gca().transAxes)
plt.xscale('log')
plt.yscale('log')

plt.tight_layout(pad=0)
plt.savefig('build/plot.pdf')
