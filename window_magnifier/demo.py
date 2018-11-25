from window_magnifier import window_magnifier
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

color = mpimg.imread('color.png')
gray = mpimg.imread('gray.png')
gray = gray.reshape((283, 283, 1))

magnifierd_color = window_magnifier(
    input_image = color,
    window_number = 2,
    magnifier_window_position = [[0, 36, 3, 46], [103, 88, 113, 98]],
    output_window_position = [[283, -20, 289, 0], [283, 283, 303, 303]],
    magnifier_times = 2
)
magnifierd_gray = window_magnifier(
    input_image = gray,
    window_number = 2,
    magnifier_window_position = [[45, 36, 55, 46], [103, 88, 113, 98]],
    output_window_position = [[-5, 280, 15, 300], [280, 280, 300, 300]],
    magnifier_times = 2
)
plt.imshow(magnifierd_color)
plt.show()
plt.imshow(magnifierd_gray)
plt.show()
