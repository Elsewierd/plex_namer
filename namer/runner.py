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


if __name__ == "__main__":
    
