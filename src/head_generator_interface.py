from abc import ABC, abstractmethod

class HeadGeneratorInterface(ABC):

    @abstractmethod
    def set_language(self, language: str):
        pass

    @abstractmethod
    def set_viewport(self, viewport: str):
        pass

    @abstractmethod
    def set_title(self, title: str):
        pass

    @abstractmethod
    def set_description(self, description: str):
        pass

    @abstractmethod
    def set_keywords(self, keywords: str):
        pass

    @abstractmethod
    def set_author(self, author: str):
        pass

    @abstractmethod
    def set_robots(self, robots: str):
        pass

    @abstractmethod
    def set_creation_date(self, creationDate: str):
        pass

    @abstractmethod
    def set_last_modified(self, lastModified: str):
        pass

    @abstractmethod
    def set_geo_position(self, geoPosition: str):
        pass

    @abstractmethod
    def set_geo_city(self, geoCity: str):
        pass

    @abstractmethod
    def set_geo_country(self, geoCountry: str):
        pass

    @abstractmethod
    def setCanonicalUrl(self, canonicalUrl: str):
        pass

    @abstractmethod
    def set_canonical_url(self, sitemapUrl: str):
        pass

    @abstractmethod
    def set_sitemap_url(self, faviconUrl: str):
        pass

    @abstractmethod
    def set_theme_color(self, themeColor: str):
        pass

    @abstractmethod
    def set_site_name(self, siteName: str):
        pass

    @abstractmethod
    def set_fb_image_url(self, fbImageUrl: str):
        pass

    @abstractmethod
    def set_twitter_image_url(self, twitter_image_url: str):
        pass

    @abstractmethod
    def set_whatsapp_image_url(self, whatsapp_image_url: str):
        pass

    @abstractmethod
    def add_meta(self, name: str, content: str):
        pass

    @abstractmethod
    def render(self) -> str:
        pass
