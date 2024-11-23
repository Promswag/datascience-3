import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    try:
        path = os.path.join("..", "ressources", "Test_knight.csv")
        df = pd.read_csv(path)
        print(len(df.columns))

        fig, axs = plt.subplots(nrows=6, ncols=5, figsize=(15, 18))

        for i in range(6):
            for j in range(5):
                axs[i, j].hist(df.iloc[:, i * 5 + j], bins=30, color='green', alpha=0.6, label='knight')
                axs[i, j].set_title(df.columns[i * 5 + j])
                axs[i, j].autoscale(enable=True, axis='both', tight=False)
                axs[i, j].legend(loc='upper right')
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.25, hspace=0.75)
        plt.show()

    except Exception as error:
        print(f'{type(error).__name__} {error}')

if __name__ == "__main__":
    main()