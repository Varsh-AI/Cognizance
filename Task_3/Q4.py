import pandas as pd
series = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
print("Before:",series)
new_series = series.map(lambda x: x[0].upper() + x[1:])
l = list([new_series[i] for i in range(0,len(new_series))])
new_string = str(' '.join(l))
print("After:",new_string)