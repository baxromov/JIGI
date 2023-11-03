import re


class VKVideoURLValidator:
    """
        VKVideoURLValidator Class for Validating VK Video URLs.

        This class provides a static method for validating VK (Vkontakte) video URLs. It checks if
        a given URL matches the expected format for VK video URLs, ensuring that it adheres to the
        pattern 'https://vk.com/video-<video_id>_<user_id>'.

        Methods:
            is_valid_vk_url(url)
                Validates a VK video URL to ensure it matches the expected format.

        Example Usage:
        --------------
        is_valid = VKVideoURLValidator.is_valid_vk_url("https://vk.com/video-12345678_98765432")
        if is_valid:
            print("Valid VK video URL")
        else:
            print("Invalid VK video URL")
    """

    @staticmethod
    def is_valid_vk_url(url):
        """
                Validates a VK video URL to ensure it matches the expected format.

                Args:
                    url (str): The URL to be validated.

                Returns:
                    bool: True if the URL matches the expected format, False otherwise.
        """
        pattern = r'https://vk.com/video-\d+_\d+'
        return bool(re.match(pattern, url))
