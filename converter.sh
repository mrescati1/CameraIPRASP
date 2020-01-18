#!/bin/bash
videoName=$1
ffmpeg -threads 4  -i "../recordings/${videoName}" -s 1280x720 -vcodec libx264 -preset ultrafast -c:a copy "../recordings_hist/{videoName}_compact.mkv"
