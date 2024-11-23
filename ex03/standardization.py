import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import os

def main():
    try:
        path = os.path.join("..", "ressources", "Train_knight.csv")
        df = pd.read_csv(path)

        scaler = StandardScaler()
        scaled_data = pd.DataFrame(scaler.fit_transform(df.drop('knight', axis=1)), columns=df.columns[:-1])
        print(scaled_data)
        scaled_data['knight'] = df['knight']

        df_sith = scaled_data[scaled_data['knight'] == 'Sith']
        df_jedi = scaled_data[scaled_data['knight'] == 'Jedi']

        fig, ax = plt.subplots()

        ax.scatter(df_sith['Empowered'], df_sith['Prescience'], color='red', alpha=0.5, label='Sith')
        ax.scatter(df_jedi['Empowered'], df_jedi['Prescience'], color='blue', alpha=0.5, label='Jedi')

        plt.show()
    except Exception as error:
        try:
            df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
            print(df)

            fig, ax = plt.subplots()
            ax.scatter(df['Empowered'], df['Prescience'], color='green', alpha=0.5, label='knight')
            plt.show()
        except Exception as error:
            print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    main()