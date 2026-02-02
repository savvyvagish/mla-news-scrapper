import pandas as pd

def export_excel(rows, filename="output.xlsx"):
    df = pd.DataFrame(rows)
    df.to_excel(filename, index=False)