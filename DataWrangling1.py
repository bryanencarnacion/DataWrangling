import pandas as bears
mathematics = {'Student': ['Ice Bear','Panda','Grizzly'],'Math': [80,95,79]};
electronics = {'Student': ['Ice Bear','Panda','Grizzly'],'Electronics': [85,81,83]};
geas = {'Student': ['Ice Bear','Panda','Grizzly'],'GEAS': [90,79,93]};
esat = {'Student': ['Ice Bear','Panda','Grizzly'],'ESAT': [93,89,88]};
MATH = bears.DataFrame(mathematics, columns=['Student','Math'])
ELECS = bears.DataFrame(electronics, columns=['Student','Electronics'])
GEAS = bears.DataFrame(geas, columns=['Student','GEAS'])
ESAT = bears.DataFrame(esat, columns=['Student','ESAT'])
m1 = bears.merge(MATH,ELECS)
m2 = bears.merge(GEAS,ESAT)
grade = bears.merge(m1,m2)
longer = bears.melt(grade,id_vars='Student',var_name='Subject',value_name='Grades')