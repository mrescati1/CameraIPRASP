ffmpeg -threads 4 -pix_fmt yuv420p  -video_size 1280x720 -i ${input_video}  -vcodec libx264 -preset ultrafast output.mkv
ffmpeg -threads 4  -input_format  -i ../recordings/2020-01-13-00-07-record.avi -s 1280x720 -preset ultrafast -c:a copy output.mkv
