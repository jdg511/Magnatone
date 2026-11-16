# Magnatone

Interactive modules and audio for the Illicit Apothecary blog post
"Magnatone's True Vibrato: Bending Pitch Before It Was Possible"
(https://illicitapothecary.com/blog/magnatones-true-vibrato-bending-pitch-before-it-was-possible).

Written and modeled at Illicit Apothecary by Jason Goldkamp.

## What is here

- `post_content_vNN.html`: the post body for each version (the text that goes into the Squarespace code block).
- `magnatone_preview_vNN.html`: a standalone preview page of the same version.
- `patch_vNN.py` / `patch_vNN.ps1`: the scripts that built each version from the one before.
- `loops/`: the audio the modules play (dry guitar loops and spring reverb impulse responses).

## Previewing a version

Run `python -m http.server 8765 --bind 127.0.0.1` in this folder, then open
`http://127.0.0.1:8765/magnatone_preview_vNN.html`.
