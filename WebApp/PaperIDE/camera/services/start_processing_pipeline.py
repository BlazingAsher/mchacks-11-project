from . import openai_process
from . import azure_tts
from . import speech_recognition


def process_image(image_base_64):
    # This is where all the processing happens!
    thestuff = openai_process.get_image_info(image_base_64)
    print(thestuff)
    # TODO:
    # - Figure out how the run the code
    # - Ask the user for voice input
    # - Speak the output to the user
    return "hehlo"