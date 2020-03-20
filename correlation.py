import seaborn as sns
sns.set(rc={'figure.figsize':(30, 30)})
corr = X.corr()
plt.figure() 
ax = sns.heatmap(corr, linewidths=.5, annot=True, cmap="YlGnBu", fmt='.1g')
plt.savefig('corr_heatmap.png')
plt.show()

# Drop highly correlated features (37->30)
columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i,j] >= 0.99:
            if columns[j]:
                columns[j] = False

feature_columns = X.columns[columns].values
drop_columns = X.columns[columns == False].values
print(feature_columns)
print('-'*73)
print(drop_columns)
