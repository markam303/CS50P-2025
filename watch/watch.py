"""Input embedded youtube iframe and output shareable youtube link"""

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(
        r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"',
        s, re.IGNORECASE)
    
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()