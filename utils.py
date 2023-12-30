import cv2
import os


# Useful utils for Image Processing course
def read_image_file_color(file):
    return cv2.imread(file, cv2.IMREAD_COLOR)


def read_image_file_grayscale(file):
    return cv2.imread(file, cv2.IMREAD_GRAYSCALE)


def write_image(filename, img):
    print(f'Writing {filename}')
    cv2.imwrite(filename, img)


def add_suffix_to_filename(filename, suffix='fl', extension=None):
    base_name, file_extension = os.path.splitext(filename)
    file_extension = extension if extension is not None else file_extension
    new_filename = os.path.join(os.path.dirname(base_name),
                                f"{os.path.basename(base_name)}_{suffix}.{file_extension}")
    return new_filename


def img_as_int(img):
    return (255 * img).astype('uint8')


def display_image(image, window_name='Result'):
    cv2.namedWindow(window_name)  # Create a named window
    cv2.moveWindow(window_name, 40, 30)  # Move it to (40,30)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def cnv_image_to_color_if_necessary(image):
    if len(image.shape) == 2:  # Grayscale
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image


def create_2x2_grid(images, convert_to_color=False):
    """
    :param images: iterable of 3 or 4 images
    :param convert_to_color: if True, then convert grayscale images to color
    :return: new image composed of 2x2 square of images . Special case: If there are only 3, then they
             will be arranged in the following order: [1,0|2,0]
    arrange images in a 2x2 grid
    """
    images = list(images)  # In case it's a generator
    if len(images) == 3:
        images = [images[1], images[0], images[2], images[0]]
    if convert_to_color:
        images = [cnv_image_to_color_if_necessary(img) for img in images]
    return cv2.vconcat([cv2.hconcat(images[0:2]),
                        cv2.hconcat(images[2:4])])


def write_images_from_dictionary(images_dct, img_filename, extension='png'):
    for suffix, img in images_dct.items():
        write_image(add_suffix_to_filename(img_filename, suffix, extension), img)
