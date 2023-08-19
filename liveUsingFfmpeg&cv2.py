import subprocess
import cv2
from datetime import datetime

# Change this line
# rtmp_url = 'rtmp://testlive-testmediaservices-inwe.channel.media.azure.net:1935/live/9ee531e6dfd74b0eb3391f0486912484/testlive'
# rtmp_url = "rtmp://ltt-testmediaservices-inwe.channel.media.azure.net:1935/live/8b9d8d6107664218aec448458a8cea5c/ltt"
# rtmp_url = "rtmp://lowtest-testmediaservices-inwe.channel.media.azure.net:1935/live/b81a5f8a5b1d473ba9952f5b11dfde2d/lowTest"
# rtmp_url = "rtmp://livestreammtm-livestream-inct.channel.media.azure.net:1935/live/34b402fb8c4948668c11ddac68af9e1c/livestreammtm"
# rtmp_url = "rtmp://prewebcamstream-livestream-inct.channel.media.azure.net:1935/live/227e55b1ad3542f6985ca52116d9118c/preWebCamStream"
rtmp_url = "rtmps://webcamstream-livestream-inct.channel.media.azure.net:2935/live/d32e324267dc42a5b90f4a32a94e0881/webCamStream"
# In my mac webcamera is 0, also you can set a video file name instead, for example "/home/user/demo.mp4"
path = 0
cap = cv2.VideoCapture(path)

# gather video info to ffmpeg
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# command and params for ffmpeg
command = ['ffmpeg',
           '-y',
           '-f', 'rawvideo',
           '-vcodec', 'rawvideo',
           '-pix_fmt', 'bgr24',
           '-s', "{}x{}".format(width, height),
           '-r', str(fps),
           '-i', '-',
           '-c:v', 'libx264',
           '-pix_fmt', 'yuv420p',   # changed
           '-preset', 'ultrafast',
           '-f', 'flv',
           rtmp_url]

# using subprocess and pipe to fetch frame data
p = subprocess.Popen(command, stdin=subprocess.PIPE)


while cap.isOpened():
    ret, frame = cap.read()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cv2.putText(frame, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1,[255, 0, 0], 2,cv2.LINE_AA)
    if not ret:
        print("frame read failed")
        break
    

    # YOUR CODE FOR PROCESSING FRAME HERE

    # write to pipe
    p.stdin.write(frame.tobytes())

p.stdin.close()  # Close stdin pipe
p.wait()  # Wait for FFmpeg sub-process to finish
cv2.destroyAllWindows()  # Close OpenCV window