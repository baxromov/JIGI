import json

from bs4 import BeautifulSoup
from pyppeteer import launch

from jigi.utils.utils import BaseGetURL


class Facebook(BaseGetURL):
    async def _start_browser(self):
        self.browser = await launch()
        self.page = await self.browser.newPage()

    async def _close_browser(self):
        await self.browser.close()

    async def _retrieve_content(self, url):
        await self.page.goto(url, {'waitUntil': 'domcontentloaded'})
        page_source = await self.page.content()
        return page_source

    def __find_all_key_values(self, data, target_key: str = 'representations'):
        results = []
        if isinstance(data, list):
            for item in data:
                results.extend(self.__find_all_key_values(item, target_key))
        elif isinstance(data, dict):
            if target_key in data:
                results.append(data[target_key])
            for value in data.values():
                results.extend(self.__find_all_key_values(value, target_key))
        return results

    def __categorize_urls(self, representations):
        result = {}

        resolutions = [360, 720, 1080]
        audio = representations[3]
        for i, representation in enumerate(representations):
            if i < len(resolutions):
                resolution = resolutions[i]
                if resolution not in result:
                    result[resolution] = {"video": "", "audio": ""}
                result[resolution]["audio"] = audio['base_url']
                result[resolution]["video"] = representation["base_url"]

        return result

    def __process(self, url):
        await self._start_browser()
        page_source = await self._retrieve_content(url)
        soup = BeautifulSoup(page_source, 'html.parser')
        data = soup.find_all('script', attrs={"type": "application/json"})
        data = list(map(lambda x: json.loads(x).get('require')[0], list(filter(lambda x: '"base_url":' in x, list(
            map(lambda x: x.text, list(filter(lambda x: '{"require":[[' in x.text, data))))))))
        await self._close_browser()
        fk = self.__find_all_key_values(data)
        return self.__categorize_urls(fk[0])

    async def getting_video_url(self, url):
        return self.__process(url)
