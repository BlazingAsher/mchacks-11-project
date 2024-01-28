from . import openai_process
from .process_code_io import process_code



def process_image(image_base_64):
    inpFileName = "input_script.py"
    outFileName = "output_script.py"
    # This is where all the processing happens!
    thestuff = openai_process.get_image_info(image_base_64)
    script_file = open(inpFileName,"w")
    # Check if 'choices' key exists in the JSON object
    if 'choices' in thestuff and isinstance(thestuff['choices'], list) and len(thestuff['choices']) > 0:
        # Accessing the 'content' field
        content_value = thestuff['choices'][0]['message']['content']
        print(thestuff['choices'][0]['message']['content'])

        # Printing the value of 'content'
        
        script_file.write(content_value)
    elif 'message' in thestuff and 'content' in thestuff['message']:
        # Alternate check if 'choices' is not present directly
        print(thestuff['message']['content'])
        content_value = thestuff['message']['content']

        # Printing the value of 'content'
        script_file.write(content_value)
    else:
        print(thestuff)
        script_file.write('print("ERROR")')
    script_file.close()

    process_code(inpFileName, outFileName)

    return "hehlo"
