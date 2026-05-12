# import pandas
import pandas as pd

# Create dictonary
data = {
    "id": [1, 2, 3],
    "name": ['A', 'B', 'C'],
    "age": [23, 22, 21]
}

# Convert into tabular format
df = pd.DataFrame(data)

# Show data
print(df)