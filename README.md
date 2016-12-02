# blender-subtitler

super simple subtitle script for blender (last used on blender v2.78)

reads an internal text file containing a very simple format for subtitles, example:

```
82:161 Hi, how are you?
298:332 I'm good, it's my birthday today.
516:560 Great I'm happy to hear that!
```

the script will manage a Text strip on your sequencer. you must create this and name it "Subtitles"

at frame 0, the script resets its internal state, which is to load the first subtitle

at each frame, the decision is made to show/hide the subtitle or advance to the next one

that's all i needed! hope it saves you time.
