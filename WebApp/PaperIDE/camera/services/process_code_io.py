import subprocess


def process_code(inFileName, outFileName):
    input_file = open(inFileName, "r")
    output_file = open(outFileName, "w")

    output_file.write("from azure_tts import speak_text\n")
    output_file.write("from speech_recognition import speech_input\n")
    output_file.write("from speech_recognition import speech_input_s\n\n")

    for line in input_file:
        line = line.replace("print(", "speak_text(")
        line = line.replace("input()", "speech_input()")
        line = line.replace('input("', 'speech_input_s("')

        output_file.write(line)

    input_file.close()
    output_file.close()

    subprocess.run(["python", outFileName])
