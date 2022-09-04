import requests 
import os
import ffmpeg

flvfile = "temprecordedstream.flv"
start_dir = "/"

def convert_to_mp4(flv_file):
    name, ext = os.path.splitext(flv_file)
    out_name = name + ".mp4"
    ffmpeg.input(flv_file).output(out_name).run()
    print("Finished converting {}".format(flv_file))

def getstream():
    streamurl = "https://pull-f5-va01.tiktokcdn.com/stage/stream-2993551701086568521_or4.flv"
    streamreq = requests.get(streamurl, stream=True, verify=False, timeout=15)
    open("temprecordedstream.flv", "wb").write(streamreq.content)

    for path, folder, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.flv'):
                print("Found file: %s" % file)
                convert_to_mp4(os.path.join(start_dir, file))
            else:
                pass



getstream()

