from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill', 
            llcrnrlat = 25, 
            llcrnrlon = -130,
            urcrnrlat = 50, 
            urcrnrlon = -60, resolution = 'l')
m.drawcoastlines()
#m.drawcountries(linewidth=2)
#m.drawstates(color = 'b')
#m.drawcounties(color = 'g')
#m.fillcontinents()
#m.etopo()
#m.bluemarble()

xs = []
ys = []

NYClat, NYClong = 40.7127, -74.0059
xpt, ypt = m(NYClong,NYClat)
xs.append(xpt)
ys.append(ys)
m.plot(xpt, ypt, 'co', markersize = 15)
  
LAlat, LAlong = 34.05, -118.25
xpt, ypt = m(LAlong,LAlat)
xs.append(xpt)
ys.append(ys)
m.plot(xpt, ypt, 'co', markersize = 15)

m.plot(xs, ys, linewidth = 3, label = 'Flight 98', color = 'r')
m.drawgreatcircle(NYClong, NYClat, LAlong, LAlat, 
                  color = 'c', linewidth = 3,
                  label = 'Arc')

plt.legend(loc = 4)
plt.title('Basemap Rendering')
plt.show()