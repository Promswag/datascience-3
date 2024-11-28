import pandas as pd
import sys

def main(str):
    try:
        df = pd.read_csv(str)
        df_validation = df.sample(frac=0.3)
        df.drop(df_validation.index, inplace=True)
        df_validation.to_csv("Validation_knight.csv", index=False)
        df.to_csv("Training_knight.csv", index=False)
    except Exception as error:
        print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a file")
        sys.exit(1)
    main(sys.argv[1])