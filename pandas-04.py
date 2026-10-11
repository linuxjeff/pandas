"""
 Como ilustrado pelo max()método, você pode fazer as coisas com um
 DataFrameou Series. pandas fornece um monte de funcionalidades, cada um deles
 um método que você pode aplicar a um DataFrameou Series. Como os métodos são
 funções, não se esqueça de usar parênteses ().
 """

import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. Willian Henry",
            "Bonell, Miss Elizabeth"

        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "famale"]
    }
)

print(df["Age"].describe())
