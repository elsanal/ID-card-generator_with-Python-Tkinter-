import select_photo
import my_directory
from sex import get_sex


def initializer():
    get_sex(None, None, None, None, None)
    select_photo.get_image(None, None, None, True)
    my_directory.get_directory('C:/Users', None, None, True)
