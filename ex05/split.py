import pandas as pd
import os

def main():
    try:
        path = os.path.join("..", "ressources", "Train_knight.csv")
        df = pd.read_csv(path)
        print(len(df))
        df_validation = df.sample(frac=0.3)
        df.drop(df_validation.index, inplace=True)
        df_validation.to_csv("Validation_knight.csv", index=False)
        df.to_csv("Training_knight.csv", index=False)

    except Exception as error:
        print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    main()