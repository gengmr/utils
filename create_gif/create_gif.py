import os
import imageio

def gif(imgs_path, save_path, duration):
    '''
    create GIF by images
    :param imgs_path: images save path
    :param save_path: 'xxx.gif'
    :param duration: interval time between two frames
    :return:
    '''
    img_number = len(os.listdir(imgs_path))
    frames = []
    for i in range(img_number):
        frames.append(imageio.imread(imgs_path + '/' + str(i + 1) + '.png'))
    imageio.mimsave(save_path, frames, 'GIF', duration=duration)

if __name__ == '__main__':
    gif(
        imgs_path='example/imgs',
        save_path='imgs.gif',
        duration=1
    )