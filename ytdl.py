import yt_dlp

def extract(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = info["formats"]

    video = max(
        [f for f in formats if f.get("ext")=="mp4" and f.get("acodec")!="none"],
        key=lambda x: x.get("filesize", 0),
        default=None
    )

    audio = max(
        [f for f in formats if f.get("vcodec")=="none"],
        key=lambda x: x.get("filesize", 0),
        default=None
    )

    return {
        "title": info["title"],
        "thumb": info["thumbnail"],
        "video": video["url"] if video else None,
        "audio": audio["url"] if audio else None
    }