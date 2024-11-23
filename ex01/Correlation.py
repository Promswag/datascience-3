import pandas as pd
import os

def main():
    try:
        path = os.path.join("..", "ressources", "Train_knight.csv")
        df = pd.read_csv(path)

        df.loc[df['knight'] == 'Jedi', 'knight'] = 1
        df.loc[df['knight'] == 'Sith', 'knight'] = 0
        df['knight'] = df['knight'].astype(int)
        correlations = df.corrwith(df['knight']).sort_values(ascending=False)
        print(correlations)

    except Exception as error:
        print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    main()