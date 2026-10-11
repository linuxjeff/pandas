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

print(df.describe())
