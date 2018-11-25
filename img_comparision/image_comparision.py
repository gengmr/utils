import numpy as np
import os
from skimage import io

def image_comparison(images):
    '''
    put all images together for better comparision, the placement mode is decided by class number, '+' represent a image
    ---------------------------------------
        if image number == 2:  + +
    ---------------------------------------
        if image number == 3:  + + +
    ---------------------------------------
        if image number == 4:  + +
                               + +
    ---------------------------------------
        if image number == 5:   + +
                               + + +
    ---------------------------------------
        if image number == 6:  + + +
                               + + +
    ---------------------------------------
        if image number == 7:     +
                                + + +
                                + + +
    ---------------------------------------
        if image number == 8:   + +
                               + + +
                               + + +
    ---------------------------------------
        if image number == 9:  + + +
                               + + +
                               + + +
    ---------------------------------------
    :param images: 4-d ndarry, (image_number, image_height, image_width, image_channel
    :return: comparision img
    '''

    assert images.shape[0] < 10 or images.shape > 1, "image number must be 2-9"
    class_number = images.shape[0]

    if class_number <= 3:
        comparision = np.hstack([images[i, :, :, :] for i in range(images.shape[0])])

    elif class_number == 4:
        comparision = np.zeros((2 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        comparision[0 : images.shape[1], images.shape[2]: 2 * images.shape[2], :] = images[0, :, :, :]
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(1, 4)])

    elif class_number == 5:
        comparision = np.zeros((2 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        left_start = int(images.shape[2] / 2)
        comparision[0 : images.shape[1], left_start: left_start + 2 * images.shape[2], :] = \
            np.hstack([images[i, :, :, :] for i in range(2)])
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(2, 5)])

    elif class_number == 5:
        comparision = np.zeros((2 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        left_start = int(images.shape[2] / 2)
        comparision[0 : images.shape[1], left_start: left_start + 2 * images.shape[2], :] = \
            np.hstack([images[i, :, :, :] for i in range(2)])
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(2, 5)])

    elif class_number == 6:
        comparision = np.zeros((2 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        comparision[0: images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(3)])
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(3, 6)])

    elif class_number == 7:
        comparision = np.zeros((3 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        comparision[0: images.shape[1], images.shape[2]: 2 * images.shape[2], :] = images[0, :, :, :]
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(1, 4)])
        comparision[2 * images.shape[1]: 3 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(4, 7)])

    elif class_number == 8:
        comparision = np.zeros((3 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        left_start = int(images.shape[2] / 2)
        comparision[0 : images.shape[1], left_start: left_start + 2 * images.shape[2], :] = \
            np.hstack([images[i, :, :, :] for i in range(2)])
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(2, 5)])
        comparision[2 * images.shape[1]: 3 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(5, 8)])

    else:
        comparision = np.zeros((3 * images.shape[1], 3 * images.shape[2], images.shape[3]))
        comparision[0: images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(3)])
        comparision[images.shape[1]: 2 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(3, 6)])
        comparision[2 * images.shape[1]: 3 * images.shape[1], :, :] = \
            np.hstack([images[i, :, :, :] for i in range(6, 9)])

    return comparision





