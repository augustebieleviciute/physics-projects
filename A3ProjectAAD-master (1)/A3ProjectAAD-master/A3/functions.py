from matplotlib import pyplot as plt
from itertools import islice


def plotList(name_plot, list_of_tuples, color, title_x, title_y):
    x = []
    y = []
    for i in list_of_tuples:
        xp= int(i[0])
        yp= float(i[1])
        x.append(xp)
        y.append(yp)
    plt.plot(x, y, color, label = name_plot)
    plt.legend()
    plt.xlabel(title_x)
    plt.ylabel(title_y)
    #print(list_of_tuples) for testing purposes

def makeList(path, col):
    path_1 = open(path, "r")
    lines = path_1.readlines()
    list_1 = []
    for i in lines:
        split_line = i.split()
        #print(split_line) testing
        tup = (split_line[0], split_line[col])
        list_1.append(tup)
    #print(list_1) #testing
    return list_1



def correctFile(Input_file, output_file):
    file_1 = open(Input_file, "r")
    file_2 = open(output_file, "w")
    lines = file_1.readlines()
    #print(lines)
    for i in lines:
        #print(i)
        splitLine = i.split()
        #print(splitLine)
        s = splitLine[0].split("/")
        # print(s)
        # print(s[0])
        second_coloumn = str(int(s[0]) + int(s[1]) / 12)
        # print(second_column)
        file_2.write(s[0] + '  ')
        file_2.write(second_coloumn + '  ')
        for x in range(1, len(splitLine)):
            file_2.write(splitLine[x] + '  ')
        file_2.write('\n')
    return output_file



def makeAverageList(inputfile, time, specify_tempCol, n):
    file = open(inputfile,'r')
    list_1 = []
    x = []
    y = []
    while True:
        #islice breaks up the data into chuncks:in this case, each chunk consists of 48 lines which we average
        next_n_lines = list(islice(file, n))
        time_x = 0
        temp_y = 0
        for i in next_n_lines:
            #print(i)
            broken = i.split()
            #print(broken[time])
            #print(broken[specify_tempCol])
            time_x += float(broken[time])
            #print(specify_tempCol)
            temp_y += float(broken[specify_tempCol])
        average_time_x = time_x / n
        average_temp_y = temp_y / n

        x.append(average_time_x)
        y.append(average_temp_y)

        tuple_1 = (average_time_x, average_temp_y)
        list_1.append(tuple_1)


        if len(next_n_lines) != n:
            file = open(inputfile,'r')
            number_of_lines = len(file.readlines())
            remainder = number_of_lines % n

            totalNumber_of_tuples_in_a_list = int((number_of_lines - remainder) / n)
            # print(totalNumber_of_tuples_in_a_list)

            list_1.pop(totalNumber_of_tuples_in_a_list) #gets rid of any remainder months if the data is not evenly spread over n number of lines
            break
        
    return list_1

def plotWithError(name, uncert, listNom, listUppY, listLowY, colCurve = 'c', colErr = 'g', xName = 'Time', yName = 'Temperature'):
    errup = []  # list of upper error y values
    errlow = []  # list of lower error y values
    xval = []  # list of x values (years)
    yval = [] # list of y values
    i = 0
    #print(listNom)
    for j in listNom:
        xval.append(float(listNom[i][0]))
        errup.append(float(listUppY[i][1]))   # creating lists for the plot of the curve and the error plots
        errlow.append(float(listLowY[i][1]))
        yval.append(float(listNom[i][1]))
        i = i + 1

    if len(errup) != len(errlow) or len(errup) != len(xval) or len(errlow) != len(xval):
        exit(2)
                    # testing if all three lists are the same length
    plt.xlabel(xName)
    plt.ylabel(yName)
    plt.fill_between(xval, errlow, errup, color = colErr, label = uncert)
    plt.plot(xval, yval, color = colCurve, label=name)
    plt.legend()


def correctData(input, output):
    input_f = open(input,'r')
    output_f=open(output,'w')
    lines= input_f.readlines()
    for i in range(0,len(lines),2):  #it skips 1 line every time (dropping the lines)
        splitLine = lines[i].split()
        #print(len(splitLine))
        for x in range(0, len(splitLine)):
            output_f.write(splitLine[x] + '  ')
        output_f.write('\n')
    return output