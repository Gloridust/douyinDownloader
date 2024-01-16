import requests
import re

class DouYinDownloader:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'cookie': 'douyin.com; ttcid=e99494eb09624587bf3bf3f1541e4b2a19;',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        self.text = requests.get(url=self.url, headers=self.headers).text


    def _get_video_url(self):
        # 使用改进的正则表达式，确保它能正确匹配所需的URL
        matches = re.findall('src(.*?)vr%3D%2', self.text)
        if matches and len(matches) > 1:
            href = matches[1]
            video_url = requests.utils.unquote(href).replace('":"', 'https:')
            return video_url
        else:
            raise ValueError("无法从提供的文本中解析视频URL")

    def download_video(self):
        video_url = self._get_video_url()
        video_content = requests.get(url=video_url).content
        # 假设你可以从URL或其他地方提取标题
        title = "downloaded_video"  # 你可以修改这里以适应实际情况
        with open(title + '.mp4', mode='wb') as f:
            f.write(video_content)

if __name__ == "__main__":
    url = input("输入抖音视频链接：")
    downloader = DouYinDownloader(url)
    try:
        downloader.download_video()
        print("视频下载完成。")
    except ValueError as e:
        print(e)
