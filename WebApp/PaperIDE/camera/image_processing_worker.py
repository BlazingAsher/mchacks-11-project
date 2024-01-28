# This is the actual file that makes stuff work!
# To avoid requests taking forever, and since all the
# web client does is submit an image, we just queue
# the image on request.
#
# Then, we have a worker running on a separate thread
# actually running the processing code, which is in
# the services module.
import queue
import threading
from .services.start_processing_pipeline import process_image

q = queue.Queue(maxsize=1)


def submit_image(image_data):
    if q.full():
        print("WARNING: already processing an image, skipping.")
        return

    q.put(image_data)


def worker():
    print("Starting image processing worker")
    while True:
        image_base64 = q.get()
        process_image(image_base64)


x = threading.Thread(target=worker, args=())
x.start()