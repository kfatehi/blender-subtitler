import bpy
import re

SUB_LIST = []

subPattern = re.compile("^(\d+):(\d+) (.+)$")
rawSubs = bpy.data.texts['subs.txt'].as_string()
for line in rawSubs.split("\n"):
    (start, end, txt) = re.search(subPattern, line).groups()
    SUB_LIST.append((int(start), int(end), txt))

subtitleTrack = bpy.data.scenes['Scene'].sequence_editor.sequences_all['Subtitles']

def setSubtitles(text):
    subtitleTrack.text = text

def clearSubtitles():
    setSubtitles("");
    

subCount = len(SUB_LIST)

pos = 0
sub = SUB_LIST[pos]
done = False

def next():
    global pos, sub, done
    pos += 1
    if pos == subCount:
        sub = None
        done = True
    else:
        sub = SUB_LIST[pos]
    
    
def my_handler(scene):
    frame = scene.frame_current
    print (done, sub, pos, frame)
    if frame == 0:
        global pos, sub, done
        pos = 0
        sub = SUB_LIST[pos]
        done = False
    if done:
        return None
    if frame < sub[0]:
        return clearSubtitles();
    if frame >= sub[0] and frame <= sub[1]:
        return setSubtitles(sub[2])
    if frame > sub[1]:
        next()
        return clearSubtitles();

# https://www.blender.org/api/blender_python_api_2_63_release/bpy.app.handlers.html
bpy.app.handlers.frame_change_pre.clear()
print("Cleared frame_change_pre handlers")
if len(SUB_LIST) > 0:
    print("Registered subtitle handler")
    bpy.app.handlers.frame_change_pre.append(my_handler)