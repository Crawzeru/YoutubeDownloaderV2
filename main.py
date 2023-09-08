import sys

import pytube


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    done = int(50 * curr / stream.filesize)
    sys.stdout.write("\r[{}{}] ".format('=' * done, ' ' * (50-done)) )
    sys.stdout.flush()


def video_downloader():

    vid_url=str(input("Enter Video URL: "))
    print('Connecting, Please wait...')
    video=pytube.YouTube(vid_url,on_progress_callback=progress_func)
    Streams=video.streams
    File_name=input('File Name:')
    Format=input('Audio Or Video :')
    path=str(input("Choose your path:(example:C:\Downloads\): "))
    if Format=='Audio' or 'audio':
        Filter=Streams.get_audio_only()
    if Format=='Video' or 'video':
        Filter=Streams.get_highest_resolution()
    print('Now downloading:',video.title)
    sizer=round(Filter.filesize/1000000)
    print('Size:',sizer,'MB')


    Filter.download(path,filename=str(File_name))
    print('Completed!')
video_downloader()