from download import download_media
from pathlib import Path


if __name__ == '__main__':

    SOURCE_URL = "https://stitcher.acast.com/livestitches/61f93dee8f523600140fabb4/1ba3a6b65e3ea741b15f06969c79c5e0.mp3?aid=61f93dee8f523600140fabb4&chid=226d4aea-cb06-4a2a-877f-8b3a037a61d9&ci=ZPSvg3tE08-spKpcgaqrIfHiui6eozlcK8xoYe1V5R9nkPtYHqojQg%3D%3D&pf=embed&sv=sphinx%401.73.2&uid=6fb0a335c40c3920ba29d03e9a22bc93&Expires=1644018658&Signature=qHNEQVH5Vxk5LCqEAAH5oYa4R7IDTyFkACbqymD0UuTTbsyM6lXWG5t1ZD-ON4nZ32I09eBrI1Od52jvW4W81yBPHk7X%7EJqjyd8oFZRtZ%7EguHFO8t5ACkO7bmQWN7I%7EWXeLjdrNBecamm37Nqq0oU5KZ1MArO9tJ3hBky9SoMTzdLsxwFbzgOWPtVKpI7fRwjYXNnjZt-Ibt9PxihkBPVtk0NPRc%7EEAD3fZuH-OUa4N3JCCTGMGw0MEy-cMQ4%7EM55u3e9L71pQQ5xSsCl7d4ImMHhHWEiJnXasNpw7selYdwzAMHoF%7E9-DhUDaBNMlXx84rFC8Pk69le2WMXrd7TJA__&Key-Pair-Id=APKAJXAFARUOTJQ3BLOQ"
    OUTPUT_DIR = Path("output").resolve()
    FILENAME = "The Exchange San Francisco Fed boss Mary Daly"
    download_media(source_url=SOURCE_URL, output_path=OUTPUT_DIR / FILENAME, extension=".mp3")