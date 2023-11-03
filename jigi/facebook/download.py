import json

from bs4 import BeautifulSoup
from pyppeteer import launch
from pyppeteer.browser import Browser

from jigi.utils.utils import BaseGetURL


class Facebook(BaseGetURL):
    _browser: Browser = None

    async def _start_browser(self):
        self._browser = await launch()
        self.page = await self._browser.newPage()

    async def _close_browser(self):
        await self._browser.close()

    async def _retrieve_content(self, url):
        await self.page.goto(url, {'waitUntil': 'domcontentloaded'})
        page_source = await self.page.content()
        return page_source

    def _find_all_key_values(self, data, target_key: str = 'representations'):
        results = []
        if isinstance(data, list):
            for item in data:
                results.extend(self._find_all_key_values(item, target_key))
        elif isinstance(data, dict):
            if target_key in data:
                results.append(data[target_key])
            for value in data.values():
                results.extend(self._find_all_key_values(value, target_key))
        return results

    def _categorize_urls(self, representations):
        result = {}

        resolutions = list(filter(lambda x: x != 0, self._find_all_key_values(representations, 'height')))
        n = list(filter(lambda x: x != 'audio/mp4', self._find_all_key_values(representations, 'mime_type')))
        audio = representations[len(n)]
        for i, representation in enumerate(representations):
            if i < len(resolutions):
                resolution = resolutions[i]
                if resolution not in result:
                    result[resolution] = {"video": "", "audio": ""}
                result[resolution]["audio"] = audio['base_url']
                result[resolution]["video"] = representation["base_url"]

        return result

    async def __process(self, url):
        await self._start_browser()
        page_source = await self._retrieve_content(url)
        soup = BeautifulSoup(page_source, 'html.parser')
        data = soup.find_all('script', attrs={"type": "application/json"})
        data = list(map(lambda x: json.loads(x).get('require')[0], list(filter(lambda x: '"base_url":' in x, list(
            map(lambda x: x.text, list(filter(lambda x: '{"require":[[' in x.text, data))))))))
        await self._close_browser()
        fk = self._find_all_key_values(data)
        return self._categorize_urls(fk[0])

    async def getting_video_url(self, url):
        return await self.__process(url)

    def _extract_urls_in_quotes(self, content):
        ...
