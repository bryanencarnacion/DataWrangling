import pandas as box
dictionary = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
df = box.DataFrame(dictionary, columns=['Box','Dimension','Value'])
tidy = df.pivot(index='Box',columns='Dimension',values='Value').reset_index()
tidy['Volume'] = tidy.Length*tidy.Width*tidy.Height