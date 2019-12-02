import pandas as pd
a = {'Student': ['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}
A = pd.DataFrame(a, columns = ['Student','Math'])
b = {'Student': ['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
B = pd.DataFrame(b, columns = ['Student','Electronics'])
c = {'Student': ['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,93]}
C = pd.DataFrame(c, columns = ['Student','GEAS'])
d = {'Student': ['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}
D = pd.DataFrame(d, columns = ['Student','ESAT'])
merge1 = pd.merge(A,B, how = 'left', on = 'Student')
merge2 = pd.merge(C,D, how = 'left', on = 'Student')
f_merge = pd.merge(merge1,merge2, how = 'left', on = 'Student')
tidy = pd.melt(f_merge,id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
tidy1 = tidy.rename(columns = {'variable':'Subject', 'value':'Grades'})
tidy2 = tidy1.sort_values('Student')
tidy3 = tidy2.reset_index()
ftidy = tidy3.drop(columns = 'index')

