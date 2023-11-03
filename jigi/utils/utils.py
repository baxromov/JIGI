from abc import ABC, abstractmethod


class BaseGetURL(ABC):
    @abstractmethod
    async def __start_browser(self):
        pass

    @abstractmethod
    async def __close_browser(self):
        pass

    @abstractmethod
    async def __retrieve_content(self, url):
        pass

    @abstractmethod
    def __extract_urls_in_quotes(self, content):
        pass

    @abstractmethod
    async def getting_video_url(self, url):
        pass
