# First exercise
# First approach (already shown):
df_galaxies = pd.DataFrame(galaxies)
df_galaxies

# split cell (Ctrl + Shift + -)
df_galaxies = df_galaxies.set_index('id')
df_galaxies

# split cell
# Second approach (using .from_records method):
df_galaxies = pd.DataFrame.from_records(galaxies, index = 'id')
df_galaxies






# Second exercise
mean_dl = galaxy_sample[has_disk_mask]['disk_length'].mean()
std_dl = galaxy_sample[has_disk_mask]['disk_length'].std()
print (mean_dl, std_dl)

# split cell
# FULL POPULATION
galaxy_sample['disk_length'].sample(n=10000).plot.hist(bins=20)#, logy = True)
plt.show()

# split cell
# SPIRAL GALAXIES
galaxy_sample[has_disk_mask]['disk_length'].sample(n=10000).plot.hist(bins=20)#, logy = True)
plt.show()

# split cell
# bulge_length for Spiral galaxies = 0
galaxy_sample.loc[has_disk_mask,'bulge_length'] = 0

# split cell
# bulge_length for elliptical galaxies
def bulge_length(mag):
    return np.exp(
        -1.145 - 0.269 * (mag - 23.)
    )

# split cell
# bulge_length for Spiral galaxies = 0
galaxy_sample.loc[~has_disk_mask,'bulge_length'] = bulge_length(galaxy_sample['app_mag'])

# split cell
galaxy_sample.tail(10)

# split cell
bl_max = 1.

# split cell
bulge_too_large_mask = ~has_disk_mask & (galaxy_sample['bulge_length'] > bl_max)

# split cell
bulge_too_large_mask.sum()

# split cell
galaxy_sample.loc[bulge_too_large_mask, 'bulge_length'].head()

# split cell
galaxy_sample.loc[bulge_too_large_mask, 'bulge_length'] = bl_max

# split cell
galaxy_sample.loc[bulge_too_large_mask, 'bulge_length'].head()

# split cell
mean_bl = galaxy_sample[~has_disk_mask]['bulge_length'].mean()
std_bl = galaxy_sample[~has_disk_mask]['bulge_length'].std()
print (mean_bl, std_bl)

# split cell
# SPIRAL GALAXIES
galaxy_sample[~has_disk_mask]['bulge_length'].sample(10000).plot.hist(bins=20)#, logy = True)
plt.show()

# split cell
bulge_and_bright_mask = ~has_disk_mask & (galaxy_sample['abs_mag'] < -21.0)

# split cell
galaxy_sample[~has_disk_mask]['abs_mag'].sample(10000).plot.hist(bins=20)#, logy = True)
plt.show()

# split cell
mean_bl = galaxy_sample[bulge_and_bright_mask]['bulge_length'].mean()
std_bl = galaxy_sample[bulge_and_bright_mask]['bulge_length'].std()
print (mean_bl, std_bl)

# split cell
# SPIRAL GALAXIES
galaxy_sample[~has_disk_mask]['bulge_length'].sample(10000).plot.hist(bins=20)#, logy = True)
plt.show()






# Third exercise
nrandom = 50

# split cell
galaxies = pd.DataFrame(data, columns=['halo_id', 'gal_id', 'ra', 'dec', 'z', 'abs_mag'])
galaxies = galaxies.set_index(['halo_id', 'gal_id'])
galaxies

# split cell
# Easy example of selecting all galaxies from one halo
galaxies.loc[3]

# split cell
galaxies.loc[1]

# split cell
galaxies.loc[1]['abs_mag'].mean()

# split cell
random_galaxies = pd.concat([galaxies]*nrandom)
random_galaxies.head(15)

# split cell
random_galaxies = random_galaxies.reset_index()
random_galaxies.head(10)

# split cell
random_galaxies.index.names = ['random_index']
random_galaxies.head(10)

# split cell
import math
random_galaxies['ra'] = 90.*np.random.random(len(random_galaxies))
random_galaxies['dec'] = (180./math.pi)*np.arccos(np.random.random(len(random_galaxies))-1)-90

# split cell
random_galaxies.head(10)






