#Machine Learning L02
#DataSet Pre-processing
#SrtaCamelo

#----------------Imports--------------------
import pandas as pd
import csv
from sklearn import preprocessing

#-------------Function Definitions----------
def change_columns(data,n):
    cols = data.columns.tolist()
    cols = cols[1:n] +cols[2:] + cols[n:n+1]
    data = data[cols]
    return data
#----------------Open File Function------------------
def openFile(path):
    f = open(path, 'r+')
    my_file_data = f.read()
    f.close()
    return my_file_data

#---------------List to Tuple-------------------
def tuplenizer(list):
    outlist = []
    for i in range(len(list)):
        tuple = (i,list[i])
        outlist.append(tuple)
    return outlist
#--------------Change Labels to numbers---------
def numberize(column,tuple):
    new_column = []
    for item in column[1:]:
        for name in tuple:
            if item == name[1]:
                new_column.append(name[0])
    return new_column
#---------------Remove White Spaces-----------------
def remove_white_sp(infile,outfile):
    with open(infile) as infile, open(outfile, 'a') as outfile:
        for line in infile:
            line = ' '.join(line.split())
            line+='\n'
            outfile.write(line)

#-------------txt to csv function-------------------
def txt_2_csv(infile,outfile, header):
    with open(outfile,'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header)
    with open(infile) as infile, open(outfile, 'a') as outfile:
        for line in infile:
            outfile.write(line.replace(' ', ','))

#------------------Remove A row function--------------

#-----------------Discretize Atributes (hot-one)----------------
def discretizer(data,column_to_disc):
    dummies = pd.get_dummies(data[column_to_disc])
    data = data.merge(dummies, left_index=True, right_index=True)
    del data[column_to_disc]
    return data

#----------------Discretie Atributes (numbered)----------------
def discretizer2(data, column_to_disc,class_tuple):
    new_column = numberize(data[column_to_disc],class_tuple)
    new_column = pd.DataFrame({'clas':new_column})
    data = data.merge(new_column, left_index=True, right_index=True)
    del data[column_to_disc]
    return data

#-------------------Normalize 0 -1 range---------------
def normalizer(data,atributes, final_column):
    #normalized_df = (data - data.min()) / (data.max() - data.min())
    for atribute in atributes:
        x = data[[atribute]].values.astype(float)
        min_max_scaler = preprocessing.MinMaxScaler()
        x_scaled = min_max_scaler.fit_transform(x)
        df_normalized = pd.DataFrame(x_scaled)
        #print(df_normalized)
        data = data.merge(df_normalized,left_index=True, right_index=True)
        del data[atribute]
    data.columns = final_column
    return data
    #print(dt_amp)
#------------------Save Data Back into csv------------

def saveCSV(data,filename):
    data.to_csv(filename, header= True, mode='w',sep=',')
#--------------Main Code--------------------

"""
#----------------IRIS -----------------------

    #-------Headers $ Columns List--------------
#path = "C:/Users/SrtaCamelo/Documents/2018.2/Machine_Pacifico/ML-L02/DataSets/original/iris_dataSet.txt"
#header = ['sepal length', 'sepal width','petal length', 'petal width','class']
#atributes_to_normalize = ['sepal length', 'sepal width','petal length', 'petal width']
final_column = ['class','sepal length','sepal width','petal length','petal width']
classes = ['Iris-setosa','Iris-versicolor','Iris-virginica']
class_tuple = tuplenizer(classes)

    #--------OutPut File names------------------
filename = "iris_dataSet.csv"
pcd_filename = 'iris_pcd_dataSet.csv'

#--file = openFile(path)
#txt_2_csv(path,filename,header)

data = pd.read_csv(filename)
#ata = normalizer(data,atributes_to_normalize,final_column)
data = discretizer2(data,'class',class_tuple)

print(data)
saveCSV(data,pcd_filename)


#------------------Shuttle Statlog-------------------
    #-------Headers $ Columns List--------------
path = "C:/Users/SrtaCamelo/Documents/2018.2/Machine_Pacifico/ML-L02/DataSets/original/statlog_dataSet.txt"
header = ['time','atribute1','atribute2','atribute3','atribute4','atribute5','atribute6','atribute7','atribute8','class']
atributes_to_normalize = ['time','atribute1','atribute2','atribute3','atribute4','atribute5','atribute6','atribute7','atribute8']
final_header = ['class','time','atribute1','atribute2','atribute3','atribute4','atribute5','atribute6','atribute7','atribute8']

    #--------OutPut File names------------------
filename = "statlog_dataSet.csv"
pcd_filename = 'C:/Users/SrtaCamelo/Documents/2018.2/Machine_Pacifico/ML-L02/DataSets/processed/numberized/statlog_pdc_dataSet.csv'

txt_2_csv(path,filename,header)
data = pd.read_csv(filename)
data = normalizer(data,atributes_to_normalize,final_header)

saveCSV(data,pcd_filename)


#------------------Yast-------------------
    #-------Headers $ Columns List--------------
path = "C:/Users/SrtaCamelo/Documents/2018.2/Machine_Pacifico/ML-L02/DataSets/original/yeast_dataSet.txt"
header = ['seq_name','mcg','gvh','alm','mit','erl','pox','vac','nuc','class']
atributes_to_normalize = ['mcg','gvh','alm','mit','erl','pox','vac','nuc']
final_header = ['class','mcg','gvh','alm','mit','erl','pox','vac','nuc']

classes = ['CYT','NUC','MIT','ME3','ME2','ME1','EXC','VAC','POX','ERL']
class_tuple = tuplenizer(classes)
    #--------OutPut File names------------------
txtfile = "yeast_dataSet_wsr.txt"
filename = "yeast_dataSet.csv"
pcd_filename = 'C:/Users/SrtaCamelo/Documents/2018.2/Machine_Pacifico/ML-L02/DataSets/processed/numberized/yeast_pdc_dataSet.csv'
"""
#-------------Glass--------------------------
"""
    # -------Headers $ Columns List--------------
path = "glass.txt"
header = ['seq_name','ri','na','mg','al','si','k','ca','ba','fe','class']
atributes_to_normalize = ['ri','na','mg','al','si','k','ca','ba','fe']
    #--------OutPut File names------------------
txtfile = "glass_dataSet_wsr.txt"
filename = "glass_dataSet.csv"
pcd_filename = filename
 #Remove White Spaces First
remove_white_sp(path,txtfile)
txt_2_csv(txtfile,filename,header)
"""
#----------------Any---------------------
"""
    # -------Headers $ Columns List--------------
path_list = ["haberman_DataSet.txt","poker_handDataSet.txt","caesarianDataSet.txt","wine_DataSet.txt","car_DataSet.txt"]
header_list = [['0','1','2','class'],['0','1','2','3','4','5','6','7''8','9','class'],
['0','1','2','3','4','class'],['class','0','1','2','3','4','5','6','7''8','9','10',"11",'12']
    ,['0','1','2','3','4','5','6','class']]
#atributes_to_normalize = ['ri','na','mg','al','si','k','ca','ba','fe']
    #--------OutPut File names------------------
txtfile_list = ["haberman_dataSet_wsr.txt","poker_hand_DataSet_wsr.txt","caesarianDataSet_wsr.txt","wine_DataSet_wsr.txt","_wsr.txt"]
filename_list = ["haberman_DataSet.csv","poker_hand_DataSet.csv","caesarianDataSet.csv","wine_DataSet.csv","car_DataSet.csv"]
#pcd_filename_list = filename_list.copy()
 #Remove White Spaces First
for i in range(4):
    path = path_list[i]
    header = header_list[i]
    txtfile = txtfile_list[i]
    filename = filename_list[i]

    remove_white_sp(path,txtfile)
    txt_2_csv(txtfile,filename,header)

    data = pd.read_csv(filename)
    saveCSV(data,filename)

#del data['seq_name']
#print(data)
#data = pd.read_csv(filename)
#data = normalizer(data,atributes_to_normalize,final_header)

#data = discretizer2(data,'class',class_tuple)
#saveCSV(data,pcd_filename)
"""

#Changes
filename = "..\DataSets\_DataSet.csv"

#data = change_columns(data,0)
#del data[data.columns[len(data.columns)-1]]
#print(reader)
#saveCSV(data,filename)


path = "car_DataSet.txt"
header = ['0','1','2','3','4','5','class']
    #--------OutPut File names------------------
txtfile = "car_DataSet_wsr.txt"
filename = "car_DataSet.csv"
pcd_filename = filename
 #Remove White Spaces First
remove_white_sp(path,txtfile)
txt_2_csv(txtfile,filename,header)

data = pd.read_csv(filename)

#saveCSV(data,pcd_filename)
clases = ['unacc', 'acc', 'good', 'vgood']
buying = ['vhigh', 'high', 'med', 'low']
maint = ['vhigh', 'high', 'med', 'low']
doors = ['2', '3', '4', '5more']
persons = ['2', '4', 'more']
lug_boot = ['small', 'med', 'big']
safety = ['low', 'med', 'high']

list_to_dic = [('0',buying), ('1',maint) ,('2',doors) ,('3',persons), ('4',lug_boot),('5',safety),('class',clases) ]

for column ,dic in list_to_dic:
    class_tuple = tuplenizer(dic)
    data = discretizer2(data, column,class_tuple )
    #print(data)
print(data)
saveCSV(data,pcd_filename)
