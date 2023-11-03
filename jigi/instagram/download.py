import re

from pyppeteer import launch
from pyppeteer.browser import Browser

from jigi.utils.utils import BaseGetURL


class Instagram(BaseGetURL):
    """
        Instagram Class for Instagram Video URLs and Metadata.

        This class is designed to scrape Instagram video URLs and their associated metadata.
        It provides methods for fetching the web page source.

        Methods:
            getting_video_url(self, url)
                Asynchronously scrapes the Instagram video page at the specified URL, extracting video metadata.

        Example Usage:
        --------------
        instagram = Instagram()
        instagram_url = "https://www.instagram.com/p/Cy0b81yRaXs/?utm_source=ig_web_copy_link"
        video_urls = await instagram.getting_video_url("https://www.instagram.com/p/Cy0b81yRaXs/?utm_source=ig_web_copy_link")
        print(video_urls)  # Display the video metadata dictionary.
        """
    browser: Browser

    async def _start_browser(self):
        self.browser = await launch(headless=True)

    async def _close_browser(self):
        if self.browser:
            await self.browser.close()

    async def _retrieve_content(self, url):
        if not self.browser:
            await self._start_browser()

        page = await self.browser.newPage()
        await page.goto(url)
        await page.waitForSelector('video')
        content = await page.content()
        return content

    def _extract_urls_in_quotes(self, content):
        url_pattern = r'"(https?://[^"]+)"'
        all_urls = re.findall(url_pattern, content)
        return all_urls

    async def getting_video_url(self, url):
        try:
            content = await self._retrieve_content(url)
            http_links = self._extract_urls_in_quotes(content)

            video_urls = [x for x in http_links if '.mp4' in x]
            if video_urls:
                video_urls = [x.replace('amp;', '') for x in video_urls]
                return video_urls, content
            else:
                return None, None
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await self._close_browser()
