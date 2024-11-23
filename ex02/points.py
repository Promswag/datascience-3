import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    try:
        path = os.path.join("..", "ressources", "Train_knight.csv")
        path2 = os.path.join("..", "ressources", "Test_knight.csv")
        df = pd.read_csv(path)
        df2 = pd.read_csv(path2)

        df_sith = df[df['knight'] == 'Sith']
        df_jedi = df[df['knight'] == 'Jedi']

        fig, axs = plt.subplots(nrows=2, ncols=2)

        axs[0, 0].scatter(df_sith['Empowered'], df_sith['Prescience'], color='red', alpha=0.5, label='Sith')
        axs[0, 0].scatter(df_jedi['Empowered'], df_jedi['Prescience'], color='blue', alpha=0.5, label='Jedi')
        axs[0, 1].scatter(df_sith['Mass'], df_sith['Midi-chlorien'], color='red', alpha=0.5, label='Sith')
        axs[0, 1].scatter(df_jedi['Mass'], df_jedi['Midi-chlorien'], color='blue', alpha=0.5, label='Jedi')
        axs[1, 0].scatter(df2['Empowered'], df2['Prescience'], color='green', alpha=0.5, label='knight')
        axs[1, 1].scatter(df2['Mass'], df2['Midi-chlorien'], color='green', alpha=0.5, label='knight')


        plt.show()

    except Exception as error:
        print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    main()