import os
import numpy as np
import matplotlib.pyplot as plt

def save_glowing_image(epoch, true_values, predicted_values, save_dir, plot_information):
    H, xedges, yedges = np.histogram2d(true_values, predicted_values, bins=(50, 50))
    plt.imshow(H.T, origin='lower', aspect='auto', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='hot')
    if plot_information:
        plt.colorbar(label='Density')
        plt.xlabel('True Values')
        plt.ylabel('Predicted Values')
        plt.title('Epoch {}: Density Plot of True vs Predicted Values'.format(epoch))
    filename = os.path.join(save_dir, 'epoch_{}.png'.format(epoch))
    plt.savefig(filename)
    plt.close()
