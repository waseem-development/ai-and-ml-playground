import pandas as pd
 
df = pd.DataFrame({
    "name":   ["Ali", "Sara", "Sara", "Omar", "Zoya"],
    "height": [170,    165,    165,    1.82,   999],  # cm
})
 
print("Number of duplicate rows:", df.duplicated().sum())  # 1
 
bad = df[(df["height"] < 100) | (df["height"] > 250)]

print("Names with invalid heights:", bad["name"].tolist())
# ['Omar', 'Zoya']
 
clean = df.drop_duplicates()

print("Number of rows after removing duplicates:", len(clean))  # 4