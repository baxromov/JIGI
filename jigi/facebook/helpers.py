import subprocess

audio_file = '1.mp4'
video_file = '2.mp4'


def make_mp4(video_file, audio_file):
    output_file = 'output_video.mp4'
    ffmpeg_cmd = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',  # Copy video codec
        '-c:a', 'aac',  # Choose an audio codec, like AAC
        '-strict', 'experimental',  # Allow the use of the experimental AAC codec
        '-map', '0:v:0',  # Map the video stream from the first input
        '-map', '1:a:0',  # Map the audio stream from the second input
        output_file
    ]
    subprocess.run(ffmpeg_cmd)
    return output_file
