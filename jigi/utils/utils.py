from abc import ABC, abstractmethod


class BaseGetURL(ABC):
    @abstractmethod
    async def _start_browser(self):
        pass

    @abstractmethod
    async def _close_browser(self):
        pass

    @abstractmethod
    async def _retrieve_content(self, url):
        pass

    @abstractmethod
    def _extract_urls_in_quotes(self, content):
        pass

    @abstractmethod
    async def getting_video_url(self, url):
        pass
