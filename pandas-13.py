import streamlit as st

import pandas as pd

titanic = pd.read_csv("titanic.csv")

ages_sex = titanic[["Age", "Sex"]]

df = ages_sex.head()

df