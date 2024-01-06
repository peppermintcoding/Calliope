"""
Functions to download and transcribe Youtube Videos
Used to transcribe all the Button Poetry Youtube Channel Videos for
training Calliope
"""


def download_yt_channels(URLS: list[str], out_dir: str):
    """Downloads all Videos from specified Youtube Channels

    URLS: list of youtube channels
    out_dir: folder to save all videos
    """
    import yt_dlp

    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }
        ],
        "paths": {"home": out_dir, "temp": "temporary"},
        "outtmpl": "%(title)s/%(autonumber)s.%(ext)s",
        "no-abort-on-error": True,
        "ignoreerrors": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        _ = ydl.download(URLS)


def transcribe_videofolder(folder_path: str, length_threshhold: int, out_filename: str):
    """Transcribes a folder of videos with Whisper

    folder_path: path with folders and videos
    lentth_threshhold: threshhold for length of videos ( for filtering out livestreams )
    out_filename: csv filename for the resulting dataframe
    """
    import os
    import pandas as pd
    from tqdm import tqdm
    from faster_whisper import WhisperModel
    from tinytag import TinyTag

    model = model = WhisperModel("tiny", compute_type="int8")

    poems = []
    for i, folder in enumerate(tqdm(os.listdir(folder_path))):
        files = os.listdir(f"{folder_path}/{folder}")
        tag = TinyTag.get(f"{folder_path}/{folder}/{files[0]}")
        if tag.duration > length_threshhold:
            continue
        segments, _ = model.transcribe(f"{folder_path}/{folder}/{files[0]}")
        text = "".join(segment.text for segment in segments)
        poems.append([i, folder, text])
        if i % 25 == 0:
            df = pd.DataFrame(
                data=poems, columns=["Index", "Video Title", "Transcribed Text"]
            )
            df.to_csv(
                out_filename,
                index=False,
                mode="a",
                header=False,
            )
            poems = []

    # save remainder
    df = pd.DataFrame(data=poems, columns=["Index", "Video Title", "Transcribed Text"])
    df.to_csv(
        out_filename,
        index=False,
        mode="a",
        header=False,
    )
