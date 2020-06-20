from matplotlib import pyplot as plt
from functions import correctFile
from itertools import islice

class Analysis:
    def __init__(self, x_title='year', y_title='Temperature anomalies', input_files=[], titles=[], list_of_tuples=[], uncert_type1='Combination of sampling and bias uncertainty',uncert_type2='Total uncertainty'):
        self.x_title = x_title
        self.y_title = y_title
        self.input_files = []
        self.titles = []
        self.list_of_tuples=[]
        self.uncert_type1 = uncert_type1
        self.uncert_type2 = uncert_type2
    def addFile(self,files, titles):
        self.input_files.append(files)
        self.titles.append(titles)
    def printAll(self):
        print(self.titles)
        print(self.input_files)
        print(self.list_of_tuples)

#tuples_1 should contain numbers(1,2,9,10,11,12)9,10,11,12 are the errors and 1, 2 are year and temp respectively

    def updateLists(self, file_index, title_index, tuples_1=(),color='', n=2, max=2017, min=1657):
        #the max and min value are my line numbers
        self.input_files
        legend= self.titles[title_index]
        file = open(self.input_files[file_index], 'r')# opening the file from the list of names above
        lines = []
        list1 = []
        x=[]
        y=[]
        for line in file:
            lines.append(line)
# I am slicing lines to only consider the rows I want to average over and writing the sliced lines in a new file
# then doing exactly the same thing that I did in makeAvrageList function from part 2

        sliced = lines[min:max]
        number_of_lines = len(sliced)
        new_file = open('zoomed in data.txt', 'w+')
        for items in sliced:
            new_file.write(items)
        new_file.close()
        new_file = open('zoomed in data.txt', 'r')

        while True:
            next_n_lines = list(islice(new_file, n))
            time_x = 0
            temp_y = 0
            errUp_1 = 0
            errLow_1= 0
            errUp_2 = 0
            errLow_2 = 0
            for i in next_n_lines:
                #print(i)
                broken = i.split()
                time_x += float(broken[tuples_1[0]])
                temp_y += float(broken[tuples_1[1]])
                errLow_1 += float(broken[tuples_1[2]])
                errUp_1 += float(broken[tuples_1[3]])
                errLow_2 += float(broken[tuples_1[4]])
                errUp_2 += float(broken[tuples_1[5]])
            average_time_x = time_x / n
            average_temp_y = temp_y / n
            average_errUp_1 = errUp_1/n
            average_errLow_1 =errLow_1/n
            averaage_errUp_2 =errUp_2/n
            average_errLow_2 =errLow_2/n
            tup =(average_time_x, average_temp_y, average_errUp_1, average_errLow_1,averaage_errUp_2, average_errLow_2)
            list1.append(tup)

            if len(next_n_lines) != n:
                p = number_of_lines % n
                totalNumber_of_tuples_in_a_list = int((number_of_lines) / n)
                list1.pop(totalNumber_of_tuples_in_a_list)

                break
        self.list_of_tuples = list1
        for coordinates in self.list_of_tuples:
            x.append(coordinates[0])
            y.append(coordinates[1])

        plt.plot(x,y,color, label= legend)
        plt.legend()
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)




    def plotWithErrors(self, dataPosition, nOfErr, colCurve='c', colErr1='g', colErr2='b'):
        self.input_files
        errup1 = []  # list of upper error y values 1
        errlow1 = []  # list of lower error y values 1
        errup2 = []
        errlow2 = []
        xval = []  # list of x values (years)
        yval = []  # list of y values
        i = 0
        # print(listNom)
        for j in self.list_of_tuples:
            xval.append(self.list_of_tuples[i][0])
            yval.append(self.list_of_tuples[i][1])
            errup2.append(self.list_of_tuples[i][2])  # extracting the data into seperate lists from the
            errlow1.append(self.list_of_tuples[i][3])  # list of tuples
            errup1.append(self.list_of_tuples[i][4])
            errlow2.append(self.list_of_tuples[i][5])
            i = i + 1

        if nOfErr == 1:  # checking the number of errors to plot
            if dataPosition == 1:  # checking the position of the data ( 9th and 10th column or 11th and 12th column)
                plt.fill_between(xval, errlow1, errup1, color=colErr1, label=self.uncert_type1)
            if dataPosition == 2:
                plt.fill_between(xval, errlow2, errup2, color=colErr2, label=self.uncert_type2)
        if nOfErr == 2:
            plt.fill_between(xval, errlow1, errup1, color=colErr1, label=self.uncert_type1)
            plt.fill_between(xval, errlow2, errup2, color=colErr2, label=self.uncert_type2)

        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)

        plt.plot(xval, yval, color=colCurve, label='test')
        plt.legend()
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)

    def scatterPlot(self, dataPosition1, dataPosition2, colorkey, x_title, y_title, input_files=[], list_of_tuples=[]):
        x_coord=[]
        y_coord=[]
        h=0
        for j in self.list_of_tuples:
            x_coord.append(self.list_of_tuples[h][0])
            y_coord.append(self.list_of_tuples[h][1])
            h=h+1

        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        plt.scatter(x_coord, y_coord, colorkey, label='Scatter')
        plt.legend()

    def Simple(self, ):
        f=open(correctFile, 'r')
        for i in f:
            data=data.sea.nh.txt.drop(data.sea.nh.txt.index[1:14]) #because the first column is the year [0], and the rest include temperature data we want to drop the lines for columns 2-14
            print(data.replace(" ", "")) #remove unwanted spaces
            data.split(' ') #seperate the data with commas










