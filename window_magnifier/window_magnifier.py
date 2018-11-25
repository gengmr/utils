from skimage import transform
import numpy as np

def window_magnifier(input_image, window_number, magnifier_window_position, output_window_position, magnifier_times):
    '''
    can magnifier several windows in input_images
    :param input_image: 3-d ndarry, image_height, image width, and image channel
    :param window_number: how many windows you want to magnifier
    :param magnifier_window_position: for example[[35, 37, 55, 57], [78, 69, 88, 79]] represent two magnifier window's
        position, 35, 37 is the x and y axes of top left corner, 55, 57 is the x and y axes of bottom right corner,
    :param output_window_position: same to manifier_window_position, but there can be negative value, for example,
    [[-35, 37, -15, 57], [78, -69, 88, -59]], negative value means it will appear on the left of on the top of the input
        image.
    :param magnifier_times: how many times you want to magnify
    :return: magnified image
    '''

    min_x = 0
    min_y = 0
    max_x = input_image.shape[0]
    max_y = input_image.shape[1]

    for i in range(window_number):
        if min(output_window_position[i][0], output_window_position[i][2]) < min_x:
            min_x = min(output_window_position[i][0], output_window_position[i][2], min_x)
        if max(output_window_position[i][0], output_window_position[i][2]) > max_x:
            max_x = max(output_window_position[i][0], output_window_position[i][2])
        if min(output_window_position[i][1], output_window_position[i][3]) < min_y:
            min_y = min(output_window_position[i][1], output_window_position[i][3])
        if max(output_window_position[i][1], output_window_position[i][3]) > max_y:
            max_y = max(output_window_position[i][1], output_window_position[i][3])

    # initialize magnifier image
    magnifier_image = np.zeros((max_x - min_x, max_y - min_y, 3))

    # calculate position of input image
    input_image_index_in_magnifier_image = [abs(min_x),
                                            abs(min_y),
                                            abs(min_x) + input_image.shape[0],
                                            abs(min_y) + input_image.shape[1]]

    print(input_image_index_in_magnifier_image)

    # calculate position of magnifier windows
    magnifier_window_index_in_magnifier_image = []
    for i in range(window_number):
        [x_left, y_down, x_right, y_up] = [abs(min_x) + magnifier_window_position[i][0],
                                           abs(min_y) + magnifier_window_position[i][1],
                                           abs(min_x) + magnifier_window_position[i][2],
                                           abs(min_y) + magnifier_window_position[i][3]]
        magnifier_window_index_in_magnifier_image.append([x_left, y_down,x_right, y_up])

    # calculate position of output windows
    output_window_index_in_magnifier_image = []
    for i in range(window_number):
        [x_left, y_down, x_right, y_up] = [abs(min_x) + output_window_position[i][0],
                                           abs(min_y) + output_window_position[i][1],
                                           abs(min_x) + output_window_position[i][2],
                                           abs(min_y) + output_window_position[i][3]]
        output_window_index_in_magnifier_image.append([x_left, y_down,x_right, y_up])

    print(output_window_index_in_magnifier_image)
    # put the input image into magnifier image
    if input_image.shape[2] == 1:
        for i in range(3):
            magnifier_image[input_image_index_in_magnifier_image[0]: input_image_index_in_magnifier_image[2],
                            input_image_index_in_magnifier_image[1]: input_image_index_in_magnifier_image[3],
                            i] = np.squeeze(input_image)
    else:
        magnifier_image[input_image_index_in_magnifier_image[0]: input_image_index_in_magnifier_image[2],
                        input_image_index_in_magnifier_image[1]: input_image_index_in_magnifier_image[3],
                        :] = np.squeeze(input_image)

    # put the magnified windows into magifier image, draw green and red bounding rectangle
    for i in range(window_number):
        patch = magnifier_image[
                magnifier_window_index_in_magnifier_image[i][0]: magnifier_window_index_in_magnifier_image[i][2],
                magnifier_window_index_in_magnifier_image[i][1]: magnifier_window_index_in_magnifier_image[i][3],
                :]
        patch = transform.resize(
            image = patch,
            output_shape = (magnifier_times * patch.shape[0], magnifier_times * patch.shape[1], patch.shape[2])
        )

        magnifier_image[
            output_window_index_in_magnifier_image[i][0]: output_window_index_in_magnifier_image[i][2],
            output_window_index_in_magnifier_image[i][1]: output_window_index_in_magnifier_image[i][3],
        :] = patch

        # draw green bounding rectangle
        magnifier_image[[magnifier_window_index_in_magnifier_image[i][0], magnifier_window_index_in_magnifier_image[i][2] - 1],
            magnifier_window_index_in_magnifier_image[i][1]: magnifier_window_index_in_magnifier_image[i][3],
            1] = 1
        magnifier_image[magnifier_window_index_in_magnifier_image[i][0]: magnifier_window_index_in_magnifier_image[i][2],
            [magnifier_window_index_in_magnifier_image[i][1], magnifier_window_index_in_magnifier_image[i][3] - 1],
            1] = 1

        # draw red bounding rectangle
        magnifier_image[[output_window_index_in_magnifier_image[i][0], output_window_index_in_magnifier_image[i][2] - 1],
            output_window_index_in_magnifier_image[i][1]: output_window_index_in_magnifier_image[i][3],
            0] = 1
        magnifier_image[output_window_index_in_magnifier_image[i][0]: output_window_index_in_magnifier_image[i][2] - 1,
            [output_window_index_in_magnifier_image[i][1], output_window_index_in_magnifier_image[i][3] - 1],
            0] = 1

    return magnifier_image



