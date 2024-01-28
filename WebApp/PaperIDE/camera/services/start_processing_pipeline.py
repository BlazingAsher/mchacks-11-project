from . import openai_process
from . import azure_tts
from . import speech_recognition


def process_image(image_base_64):
    # This is where all the processing happens!
    thestuff = openai_process.get_image_info(image_base_64)
    f = open("script.py","w")
    # Check if 'choices' key exists in the JSON object
    if 'choices' in thestuff and isinstance(thestuff['choices'], list) and len(thestuff['choices']) > 0:
        # Accessing the 'content' field
        content_value = thestuff['choices'][0]['message']['content']
        print(thestuff['choices'][0]['message']['content'])

        # Printing the value of 'content'
        
        f.write(content_value)
    elif 'message' in thestuff and 'content' in thestuff['message']:
        # Alternate check if 'choices' is not present directly
        print(thestuff['message']['content'])
        content_value = thestuff['message']['content']

        # Printing the value of 'content'
        f.write(content_value)
    else:
        f.write('print("ERROR")')
    f.close()
    # TODO:
    # - Figure out how the run the code
    # - Ask the user for voice input
    # - Speak the output to the user
    return "hehlo"
