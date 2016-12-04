import bpy
import re

class Subtitler():
    def __init__(self):
        subPattern = re.compile("^(\d+)-(\d+) (.+)$")
        self.SUB_LIST = []
        rawSubs = bpy.data.texts['subs.txt'].as_string()
        for line in rawSubs.split("\n"):
            try:
                (start, end, txt) = re.search(subPattern, line).groups()
                self.SUB_LIST.append((int(start), int(end), txt))
            except AttributeError:
                pass
            
    def getSubtitlesList(self):
        return self.SUB_LIST
    
    def addStripsToChannel(self, ch):
        scene = bpy.data.scenes['Scene']
        seqs = scene.sequence_editor.sequences
        for (start, end, txt) in self.getSubtitlesList():
            name = "sub"+str(start)
            strip = seqs.new_effect(name, "TEXT", ch, start, end)
            strip.text = txt
            strip.wrap_width = 1
            strip.blend_type = "ADD"

Subtitler().addStripsToChannel(3)