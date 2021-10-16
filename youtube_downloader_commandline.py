# Youtube video downloader by Zothan Sanga
# For any question reachout to sanga3055@gmail.com
# First rev: Sunday 17 Oct 2021

# For complete pytube library check https://buildmedia.readthedocs.org/media/pdf/python-pytube/latest/python-pytube.pdf 
# Example video: https://www.youtube.com/watch?v=2XN-u0fsSLw

from pytube import YouTube

URL = input("Enter a video URL: ")  # Get user input
video = YouTube(URL) # Instantiate the Youtube Object with the Url of the Video
video_streams = video.streams

'''Due to youtube algorithm DASH change, 720P and below can only be downloaded with video and audio compbine
 for 720p and above we need to download the video and audio separately
'''

# Get all mp4 video streams from the URL entered by the user
mp4_video_stream = video_streams.filter(file_extension = "mp4").filter(progressive=True)

#get the highest & lowest resolution 
highest_res = mp4_video_stream.get_highest_resolution()
lowest_res = mp4_video_stream.get_lowest_resolution()

print("\n highest resolution is : ", highest_res)
print("\n lowest resolution is : ",lowest_res,"\n")

#print the video Title
print("Video Title is :",video.title)

#function to check the length of the video
video_len = video.length

def sec_to_hours(seconds):
    a=str(seconds//3600) # a is to get duration of video in hours
    b=str((seconds%3600)//60) # b is to get duration of video in Minutes
    c=str((seconds%3600)%60) # c is to get duration of video in seconds
    d=["{} hours {} mins {} seconds".format(a, b, c)]
    return d

print("Video Length is :",sec_to_hours(video_len))

# Download the user's choice of resolution

download_yes_or_no = input(f"Do you want to download the video, enter y or n : ")

if download_yes_or_no == "y":
    print("\n Initiate downloading!!")
    high_or_low_res = input(f"Do you want to download the video in highest(h) or lowest(l) quality available , enter h or l : ")
    if high_or_low_res == "h":
        print("Downloading high resolution >>>")
        highest_res.download()
        print(video.title, "---> has been downloaded in the highest available quality\n")
    else:
        if high_or_low_res == "l":
            print("Downloading lower quality video >> ")
            lowest_res.download()
            print(video.title, "--> has been downloaded in the lowest available quality\n")

        else:
            print("\n Not a valid input, exiting!!\n")
            exit()

else:
    if download_yes_or_no == "n":
        print("\nYou choose No, Quitting!!\n")
        exit()
    else:
        print("\n Not a valid input, exitting \n")
        exit()




#print(video_streams) # Print the available video streams
#print("\n mp4 filter:---->>> ",video_streams.filter(file_extension='mp4')) # Print the available mp4 video streams

# Check for the available resolution 360p, 720p and 1080p

# video_file = YouTube(video_link).streams.filter(res="720p").order_by('resolution').desc().first().download()

# download ---> video.streams.get_by_itag(18).download()
