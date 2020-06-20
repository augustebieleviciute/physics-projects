from functions import makeList
from functions import plotList
from functions import correctFile
from functions import makeAverageList
from functions import plotWithError
from matplotlib import pyplot as plt
from classes import Analysis


SRCDIR='J:\\Physics\\Teaching\\spa4601\\Materials\\'
DESTDIR='G:\\'

#Part 1 testing
#checking if makeList creates the list
test = makeList('J:\\Physics\\Teaching\\spa4601\\Materials\\Data.nh.txt',1)
print(test)
plot = plotList("North Hemisphere",test, 'purple', "Year","Temperature anomalies")
plt.savefig('test.png')
plt.show()


#Part 2 correctfile() function test
#testing if the file is being corrected and the data is being written into the file properly
#The corrected output file is saved in the path shown above DESTDIR(destination directory)

test_file= correctFile(SRCDIR+"Data.monthly_nh.txt", DESTDIR+"Corrected.Data.monthly_nh.txt")
#I checked my drive and the file has been saved correctly

#Part 2 testing makeAveragelist() function along with plotlist 3 times with 3 different averaging period

#running the function first time with average period of 2
#Then I printed the list of tuples to see if my function is averaging properly
#I have chosen to use 2 as my period to average over because this will allow me to test my x and y points using a calculator
#That way I can check if my function is calculating my values correctly
#I have done the same thing for the rest of the 2 tests using 3 and 4 as my averageing peiod

test_list_1= makeAverageList(DESTDIR+"Corrected.Data.monthly_nh.txt", 1, 2, 120)
plotWithError('test', 'test unc', test_list_1, makeList("G:\\Corrected.Data.monthly_nh.txt", 8), makeList("G:\\Corrected.Data.monthly_nh.txt", 9), colCurve = 'c', colErr = 'g', xName = 'Time', yName = 'Temperature')
plt.show()
print(test_list_1) # printing my list of tuples containing my x and y values
#plot_1= plotList("North Hemisphere",test_list_1, 'red', "Year","Temperature")
print(test_list_1) #testing again to make sure the correct tuples have been passed to the plotList function


#Running 2nd time with avearage period of 3
test_list_2= makeAverageList(DESTDIR+"Corrected.Data.monthly_nh.txt", 1, 2, 120)
plotWithError('test', 'test unc', test_list_2, makeList("G:\\Corrected.Data.monthly_nh.txt", 8), makeList("G:\\Corrected.Data.monthly_nh.txt", 9), colCurve = 'c', colErr = 'g', xName = 'Time', yName = 'Temperature')
plt.show()
print(test_list_2)
#plot_2= plotList("North Hemisphere",test_list_2, 'blue', "Year","Temperature")
print(test_list_2)


#running 3rd time with average period of 4
#using a caloculator to check for the first few values to see if they are being calculated correctly
test_list_3= makeAverageList(DESTDIR+"Corrected.Data.monthly_nh.txt", 1, 2, 120)
plotWithError('test', 'test unc', test_list_3, makeList("G:\\Corrected.Data.monthly_nh.txt", 8), makeList("G:\\Corrected.Data.monthly_nh.txt", 9), colCurve = 'c', colErr = 'g', xName = 'Time', yName = 'Temperature')
plt.show()
print(test_list_3)
#plot_3= plotList("North Hemisphere",test_list_2, 'black', "Year","Temperature")
print(test_list_3)


###testing classes functions
file_1 = Analysis()
file_n = correctFile(SRCDIR+"Data.monthly_nh.txt", DESTDIR+"Corrected.Data.monthly_nh.txt")
file_s= correctFile(SRCDIR+"Data.monthly_sh.txt", DESTDIR+"Corrected.Data.monthly_sh.txt")
file_t= correctFile(SRCDIR+"Data.monthly_tropical.txt", DESTDIR+"Corrected.Data.monthly_tropical.txt")

# appending correct files to the addFile function
file_1.addFile(file_n, 'North hemisphere')
file_1.addFile(file_s, 'South hemisphere')
file_1.addFile(file_t, 'Tropical')


file_1.updateLists(0, 0, tuples_1=(1,2,8,9,10,11), color='darkcyan')
file_1.printAll()# printing titles, file names and updated list (the list of tuples is only for one file from the 3 files)
#to see if the list is updating by changing the file-index which selects different files from the list of files

file_1.plotWithErrors(0, 2)
#plt.show()