import argparse
from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript(url: str) -> None:
    """
    Extract transcript from a youtube video
    :param url: Youtube video url
    """
    video_id = url.split("watch?v=")[1]
    captions = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    for caption in captions:
        print(caption['text'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract transcript from youtube video')
    parser.add_argument('url', type=str, help='Youtube video url')
    args = parser.parse_args()
    extract_transcript(args.url)
