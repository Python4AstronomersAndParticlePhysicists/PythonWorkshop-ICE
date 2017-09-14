# Exercise Astropy 1
speed_of_earth_2 = np.sqrt(const.G * const.M_sun / const.au) 
speed_of_earth_2.to('km/s')


# Exercise Astropy 2
plt.plot(10**sdss_qso_hdulist['COADD'].data['loglam'], gaussian_filter(y_values_masked, sigma=16), 
         color='orange', linewidth=3)
plt.xlabel('Wavelengths (Angstroms)')
plt.ylabel(r'f$\lambda$ (erg/s/cm2/A)')

for eline in sdss_qso_hdulist['SPZLINE'].data:
    if eline['LINECHI2'] > 0:
        line_wl = eline['LINEWAVE'] * (1 + eline['LINEZ'])
        plt.axvline(x=line_wl, color='red', alpha=0.6)
        plt.text(line_wl, 
                 eline['LINECONTLEVEL'] * 0.7,
                 eline['LINENAME'])
        

# Exercise Astropy 3
# Convert coordinates to pixel positions
gaia_x, gaia_y = hst_image_wcs.all_world2pix(gaia_hdulist[1].data['ra'],
                                             gaia_hdulist[1].data['dec'],
                                             origin)

# Plot the image
norm = ZScaleInterval()
vmin, vmax = norm.get_limits(hst_hdulist[0].data)
plt.imshow(hst_hdulist[0].data, vmin=vmin, vmax=vmax, interpolation='none', origin='lower')
plt.colorbar()

# Plot the sources
plt.scatter(gaia_x, gaia_y, alpha=0.5, marker='o')

# Focus over the region of interest
plt.xlim([0,1000])
plt.ylim([0,700])

###########################

#Exercise Photutils 1:
phot_table_local_bkg.add_index('id')
very_different = phot_table_local_bkg.iloc[phot_table_local_bkg['residual_aperture_sum'] * 1.5
                                           < phot_table_global_bkg['aperture_sum']]

quite_similar = phot_table_local_bkg.iloc[phot_table_local_bkg['residual_aperture_sum'] * 1.5
                                           > phot_table_global_bkg['aperture_sum']]

my_python_ds9(sdss_g_hdu_list[0].data)
plt.scatter(very_different['xcenter'], very_different['ycenter'], c='red', alpha=0.5)
plt.scatter(quite_similar['xcenter'], quite_similar['ycenter'], c='limegreen', alpha=0.5)


#Exercise Photutils 2:
g = float(sdss_g_hdu_list[0].header['EXPTIME'])
aperture_area = apertures.area()  # or also = math.pi * aperture_radius**2
F = phot_table_local_bkg['aperture_sum_1'][source_num] - (median_clipped * aperture_area)
sigma_F = np.sqrt((F / g) + (aperture_area * std_clipped ** 2))

print (phot_table_local_bkg['aperture_sum_1'][source_num],  sigma_F)
    