import asyncio
import re

from bs4 import BeautifulSoup
from pyppeteer import launch
from pyppeteer.browser import Browser

from jigi.utils.utils import BaseGetURL


class VK(BaseGetURL):
    """
    VK Class for VK Video URLs and Metadata.

    This class is designed to scrape VK (Vkontakte) video URLs and their associated metadata.
    It provides methods for fetching the web page source, retrieving video URLs in various
    qualities (e.g., url240, url360, etc.).

    Attributes:
        result_object (dict): A dictionary to store the scraped video metadata.
        desired_keys (list): A list of desired keys representing video quality (e.g., "url240").

    Methods:
        getting_video_url(self, url)
            Asynchronously scrapes the VK video page at the specified URL, extracting video metadata.

    Example Usage:
    --------------
    vk = VK()
    vk_url = "https://vk.com/video-12345678_98765432"
    video_urls = await extractor.getting_video_url("https://vk.com/video-12345678_98765432")
    print(video_urls)  # Display the video metadata dictionary.
    """
    _browser: Browser = None

    def __init__(self):
        self.result_object = {}
        self.desired_keys = ["url240", "url360", "url480", "url720", "url1080"]

    async def _start_browser(self):
        self._browser = await launch()

    async def _close_browser(self):
        if self._browser:
            await self._browser.close()

    async def _retrieve_content(self, url):
        browser = self._browser
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'domcontentloaded'})
        page_source = await page.content()
        return page_source

    def _extract_urls_in_quotes(self, content):
        parsed_data = {}
        for key in self.desired_keys:
            match = re.search(f'"{key}"\s*:\s*"([^"]*)"', content)
            if match:
                parsed_data[key] = match.group(1).replace('\\', '')
        return parsed_data

    async def getting_video_url(self, url):
        page_source = await self._retrieve_content(url)
        if page_source:
            try:
                soup = BeautifulSoup(page_source, 'html.parser')
                javascript_scripts = soup.find_all('script', type='text/javascript')

                parsed_data_list = await asyncio.gather(
                    *(self._extract_urls_in_quotes(script.text) for script in javascript_scripts)
                )

                for parsed_data in parsed_data_list:
                    self.result_object.update(parsed_data)

            except Exception as e:
                print(f"Error while parsing page source: {e}")
        return self.result_object
