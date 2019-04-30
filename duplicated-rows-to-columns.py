import pandas

a = pd.DataFrame(dict(col1=list('112233'), col2=list('121212'), 
                      col3=list('abcdef'), col4=list('abcdef')))
display(a)
a.set_index(['col1', 'col2']).unstack().reset_index()
