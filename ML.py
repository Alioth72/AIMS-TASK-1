import pandas as pd
data = {
    'Colour': ['red', 'green', 'blue','red','red','green']
}
df = pd.DataFrame(data)
def ordinal_encoding(df,column):
    unique = (df[column].unique())
    cat_in = {category :index for index, category in enumerate(unique)}
    df[column + '_ordinal'] = df[column].map(cat_in)
    return df, cat_in
df_final, map = ordinal_encoding(df,'Colour')
print(df_final)
print(map)

def one_hot_encoding(df,column):
    one_hot = pd.get_dummies(df[column], prefix = column)
    df = pd.concat([df,one_hot], axis=1)
    return df
final2 = one_hot_encoding(df_final,'Colour')
print(final2)


