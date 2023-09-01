
#import argparse
from pydub import AudioSegment
import random

class AuCutConfig:
    def __init__(self):
        self.output_file_name = "aucut.mp3"
        self.avg_segment_length = 2000 # in ms
        self.variability = 0
        self.rando_seed = ""

    def setConfig(self): # from command line
        print("sorry no can do, using defaults!")
    
class AuCut:
    def __init__(self):
        self.config = AuCutConfig()
        self.output_file = AudioSegment.empty()
    def configure(self, c):
        self.config = c
    def openAudioFiles(self):
        self.audio_1 = AudioSegment.from_file("test/TT64.mp3", format="mp3")
        self.audio_2 = AudioSegment.from_file("test/TheEight.mp3", format="mp3")
        self.audio_3 = AudioSegment.from_file("test/rjs.mp3", format="mp3")
        print("opened!")
    def cutAndMergeFiles(self):
        print("cutting up!")
        # tuples so the len is only calculated once
        afiles = [[self.audio_1, len(self.audio_1)], [self.audio_2, len(self.audio_2)], [self.audio_3, len(self.audio_3)]]
        # 60 second output file
        while len(self.output_file)/1000 < 60:
            # select one of the input files at random
            f = random.choice(afiles)
            # select a random slice from the file
            portion_start = random.randint(0, f[1])
            # grab 2 seconds
            portion = f[0][portion_start:portion_start+self.config.avg_segment_length]
            if len(self.output_file) > 50:
                self.output_file = self.output_file.append(portion, 50)
            else:
                self.output_file = self.output_file.append(portion, 0)

    def writeFile(self):
        print("let's write it!")
        #file_handle = self.audio_1.export("test/foo.mp3", format="mp3") 
        file_handle = self.output_file.export("test/"+self.config.output_file_name, format="mp3")
        file_handle.flush()
        file_handle.close()

def main():
    print("hello!")
    cutter = AuCut()
    cutter.openAudioFiles()
    cutter.cutAndMergeFiles()
    cutter.writeFile()

if __name__ == "__main__":
    main()