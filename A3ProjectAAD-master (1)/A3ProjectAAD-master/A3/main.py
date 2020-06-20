from functions import makeList
from functions import plotList
from functions import correctFile
from functions import makeAverageList
from functions import plotWithError
from matplotlib import pyplot as plt
from classes import Analysis


SRCDIR='J:\\Physics\\Teaching\\spa4601\\Materials\\'
DESTDIR='G:\\'

####part 1
list = makeList('J:\\Physics\\Teaching\\spa4601\\Materials\\Data.nh.txt', 1)
plot= plotList('North hemisphere', list, 'slateblue', 'year', 'temperature anomalies')
plt.savefig('A3part1.png')
plt.show()

####Part 2
file_22 = correctFile(SRCDIR+"Data.monthly_nh.txt", DESTDIR+"Corrected.Data.monthly_nh.txt")
file_23 = correctFile(SRCDIR+"Data.monthly_ns.txt", DESTDIR+"Corrected.Data.monthly_ns.txt")
file_24 = correctFile(SRCDIR+"Data.monthly_sh.txt", DESTDIR+"Corrected.Data.monthly_sh.txt")
file_25 = correctFile(SRCDIR+"Data.monthly_tropical.txt", DESTDIR+"Corrected.Data.monthly_tropical.txt")

#I ran it with different values of n and saved the graphs
n = 48 #4 years
graph = makeAverageList(file_22, 1, 2, n)
plot= plotList('North hemisphere',graph, 'purple', 'year', 'temperature anomalies')
graph1=makeAverageList(file_23, 1, 2, n)
plot= plotList('ns',graph1,'darkcyan', 'year', 'temperature anomalies')
graph2=makeAverageList(file_24, 1, 2, n)
plot= plotList('South hemisphere',graph2, 'blue', 'year', 'temperature anomalies')
graph3=makeAverageList(file_25, 1, 2, n)
plot= plotList('Tropical',graph3, 'black', 'year', 'temperature anomalies')
plt.savefig('A3part2a.png')
plt.show()


#plotting all 4 graphs with errors averaging over n yaers
plotWithError('Data monthly nh', 'Total Uncertainty', makeAverageList(file_22, 1, 2, n), makeAverageList(file_22, 1, 11, n), makeAverageList(file_22, 1, 12, n), colCurve = 'red', colErr = 'darksalmon')
plotWithError('Data monthly nh', 'Measurement, sampling and bias Uncertainties', makeAverageList(file_22, 1, 2, n), makeAverageList(file_22, 1, 9, n), makeAverageList(file_22, 1, 10, n), colCurve = 'red', colErr = 'sienna')
plt.savefig('A3part2b.png')
plt.show()

plotWithError('Data monthly ns', 'Total Uncertainty', makeAverageList(file_23, 1, 2, n), makeAverageList(file_23, 1, 11, n), makeAverageList(file_22, 1, 12, n), colCurve = 'darkblue', colErr = 'paleturquoise')
plotWithError('Data monthly ns', 'Measurement, sampling and bias Uncertainties', makeAverageList(file_23, 1, 2, n), makeAverageList(file_23, 1, 9, n), makeAverageList(file_23, 1, 10, n), colCurve = 'darkblue', colErr = 'darkcyan')
plt.savefig('A3part2c.png')
plt.show()

plotWithError('Data monthly sh', 'Total Uncertainty', makeAverageList(file_24, 1, 2, n), makeAverageList(file_24, 1, 11, n), makeAverageList(file_24, 1, 12, n), colCurve = 'purple', colErr = 'pink')
plotWithError('Data monthly sh', 'Measurement, sampling and bias Uncertainties', makeAverageList(file_24, 1, 2, n), makeAverageList(file_24, 1, 9, n), makeAverageList(file_24, 1, 10, n), colCurve = 'purple', colErr = 'hotpink')
plt.savefig('A3part2d.png')
plt.show()

plotWithError('Data monthly tropical', 'Total Uncertainty', makeAverageList(file_25, 1, 2, n), makeAverageList(file_25, 1, 11, n), makeAverageList(file_25, 1, 12, n), colCurve = 'k', colErr = 'lightgray')
plotWithError('Data monthly tropical', 'Measurement, sampling and bias Uncertainties', makeAverageList(file_25, 1, 2, n), makeAverageList(file_25, 1, 9, n), makeAverageList(file_25, 1, 10, n), colCurve = 'k', colErr = 'gray')
plt.savefig('A3part2e.png')
plt.show()


####Part 3
file_n = correctFile(SRCDIR + "Data.monthly_nh.txt", DESTDIR + "Corrected.Data.monthly_nh.txt")
file_s = correctFile(SRCDIR + "Data.monthly_sh.txt", DESTDIR + "Corrected.Data.monthly_sh.txt")
file_t = correctFile(SRCDIR + "Data.monthly_tropical.txt", DESTDIR + "Corrected.Data.monthly_tropical.txt")


file_1= Analysis() #creating an instance

#adding corrected file
file_1.addFile(file_n, 'North hemisphere')
file_1.addFile(file_s, 'South hemisphere')
file_1.addFile(file_t, 'Tropical')


#graph for the last 10 years
file_1.updateLists(0, 0, tuples_1=(1,2,8,9,10,11), color='purple', max= 2017, min= 1897)
file_1.updateLists(1, 1, tuples_1=(1,2,8,9,10,11), color='green',max= 2017, min= 1897)
file_1.updateLists(2, 2, tuples_1=(1,2,8,9,10,11), color='black',max= 2017, min= 1897)
plt.savefig("A3part3(10 years).png")
plt.show()


# for the last 30years
#the max and min is already set as default argument in classes.py for 30 years
#therefore, I do not need to specify them like I did for 10 years
file_1.updateLists(0, 0, tuples_1=(1,2,8,9,10,11), color='darkcyan')
file_1.updateLists(1, 1, tuples_1=(1,2,8,9,10,11), color='purple')
file_1.updateLists(2, 2, tuples_1=(1,2,8,9,10,11), color='black')
plt.savefig("A3part3(30 years).png")
plt.show()


