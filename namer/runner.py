import json
import cv2


def plex_compatable(file: str) -> bool:
    try:
        video = cv2.VideoCapture(file)
    except cv2.error as e:
        # TODO: write class FileTypeException(Exception):
        raise FileTypeException(
            f"cv2 Cannot use file: {file}", additional_info={"file": file}
        )
    else:
        # TODO: what needs to be checked goes here
        container = video.get(cv2.CAP_PROP_FORMAT)
        resolution = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        video_codec = video.get(cv2.CAP_PROP_FOURCC)
        framerate = video.get(cv2.CAP_PROP_FPS)
        bit_depth = video.get(cv2.CAP_PROP_BITSPERPIXEL)
        audio_codec = video.get(cv2.CAP_PROP_FOURCC)
        audio_channels = video.get(cv2.CAP_PROP_CHANNEL)
        bitrate = video.get(cv2.CAP_PROP_BITRATE)
    finally:
        # Release the video capture object, if it was opened
        video.release()

def preferences_load(filepath: str, *args) -> str:
    """Loads prefernces from file, if there are no *args returns the whole file as a string

    Args:
        filepath (str): Filepath to JSON file to be loaded from.
        *args (tuple): Keys needed to navigate to the value(s)

    Raises:
        KeyError: The keys do not exisit in the called order.
        e: Exception caught if filepath does not open properly.

    Returns:
        str: The portion of the JSON file dictated by the keys (args).
    """    
    try:
        with open(filepath, "r") as file_json:
            data = json.load(file_json)
            for arg in args:
                if data.get(arg) is None:
                    raise KeyError(f"Error in the preference keys: {args}")
                data = data[arg]
            
            return str(data)
    except Exception as e:
        raise e

def preference_save(filepath:str, value:Any=None, create:bool=False, *args) -> None:
    """Saves a prefence value to file

    Args:
        filepath (str): Filepath to JSON file to be altered.
        value (Any, optional): Value to be saved. Defaults to None.
        create (bool, optional): Boolean flag denoting weather to create . Defaults to False.
        *args (tuple): Keys needed to navigate to the value

    Raises:
        KeyError: If create is not True and the keys do not exisit in the called order.
        e: Exception caught if filepath does not open properly.
    """    
    try:
        with open(filepath, "r") as file_json:
            data = json.load(file_json)
        
        current_level = data
        for i, arg in enumerate(args):
            if not create and current_level.get(arg) is None:
                raise KeyError(f"Error in the preference keys: {args}")
            elif i == len(args) - 1:
                # If it's the last key, set the value
                current_level[arg] = value
            else:
                # If it's not the last key, update the current level
                current_level = current_level.setdefault(arg, {})
        
        with open(filepath, "w") as file_json:
            json.dump(data, file_json, indent=2)
    except Exception as e:
        raise e
if __name__ == "__main__":
...
