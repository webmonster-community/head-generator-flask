from typing import Optional


class head_generator:
    def __init__(self) -> object:
        self.language = 'en'
        self.viewport = 'width=device-width, initial-scale=1'
        self.title = ''
        self.description = ''
        self.keywords = ''
        self.author = ''
        self.robots = 'index, follow'
        self.creation_date = ''
        self.last_modified = ''
        self.geo_lat = ''
        self.geo_lng = ''
        self.geo_city = ''
        self.geo_country = ''
        self.canonical_url = ''
        self.sitemap_url = '/sitemap.xml'
        self.favicon_url = '/favicon.png'
        self.theme_color = '#ffffff'
        self.site_name = ''
        self.fb_image_url = ''
        self.twitter_image_url = ''
        self.whatsapp_image_url = ''
        self.stylesheet_urls = []
        self.script_urls = []
        self.metatags = []

    def get_canonical_link(self):
        if not hasattr(self, '_SERVER'):
            return False
        url = self._SERVER['REQUEST_URI']
        url = url.rstrip('/')
        return '{}://{}{}'.format('https' if self._SERVER.get('HTTPS') != 'off' else 'http', self._SERVER['HTTP_HOST'], url)

    def set_language(self, language):
        self.language = language
        return self

    def set_viewport(self, viewport):
        self.viewport = viewport
        return self

    def set_title(self, title):
        self.title = title
        return self

    def set_description(self, description):
        self.description = description
        return self

    def set_keywords(self, keywords):
        self.keywords = keywords
        return self

    def set_author(self, author):
        self.author = author
        return self

    def set_robots(self, robots):
        self.robots = robots
        return self

    def set_creation_date(self, creation_date):
        self.creation_date = creation_date
        return self

    def set_last_modified(self, last_modified):
        self.last_modified = last_modified
        return self

    def set_geo_lat(self, geo_lat):
        self.geo_lat = geo_lat
        return self

    def set_geo_lng(self, geo_lng):
        self.geo_lng = geo_lng
        return self

    def set_geo_city(self, geo_city):
        self.geo_city = geo_city
        return self

    def set_geo_country(self, geo_country):
        self.geo_country = geo_country
        return self

    def set_canonical_url(self, canonical_url):
        self.canonical_url = canonical_url
        return self

    def set_sitemap_url(self, sitemap_url):
        self.sitemap_url = sitemap_url
        return self

    def set_favicon_url(self, favicon_url):
        self.favicon_url = favicon_url
        return self

    def set_theme_color(self, theme_color):
        self.theme_color = theme_color
        return self

    def set_site_name(self, site_name):
        self.site_name = site_name
        return self

    def set_fb_image_url(self, fb_image_url):
        self.fb_image_url = fb_image_url
        return self

    def set_twitter_image_url(self, twitter_image_url):
        self.twitter_image_url = twitter_image_url
        return self

    def set_whatsapp_image_url(self, whatsapp_image_url):
        self.whatsapp_image_url = whatsapp_image_url
        return self

    def add_stylesheet_urls(self, url):
        self.stylesheet_urls.append(url)
        return self

    def add_script_urls(self, url):
        self.script_urls.append(url)
        return self

    def add_meta(self, name: str, content: str) -> 'head_generator':
        self.metatags.append({'name': name, 'content': content})
        return self

    def add_content(self, format_str: str, value: str) -> str:
        return f"{format_str}\n".format(value) if value else ''

    def get_external_domain_url(self, url: str) -> Optional[str]:
        from urllib.parse import urlparse
        url_parts = urlparse(url)
        if not all([url_parts.scheme, url_parts.netloc]):
            return None
        external_domain_url = url_parts.scheme + '://' + url_parts.netloc
        import os
        current_domain_url = f"{'https' if os.environ.get('HTTPS') == 'on' else 'http'}://{os.environ.get('HTTP_HOST')}"
        if external_domain_url != current_domain_url:
            return external_domain_url
        return None

    def render(self) -> str:
        html = '<!DOCTYPE html>\n'
        html += '<html lang="{}">\n'.format(self.language)
        html += '<head>\n'
        html += '    <meta charset="UTF-8">\n'
        html += self.add_content('    <meta name="viewport" content="{}">', format(self.viewport))
        html += self.add_content('    <meta name="language" content="{}">', format(self.language))
        html += self.add_content('    <title>{}</title>', format(self.title))
        html += self.add_content('    <meta name="description" content="{}">', format(self.description))
        html += self.add_content('    <meta name="keywords" content="{}">', self.keywords)
        html += self.add_content('    <meta name="author" content="{}">', self.author)
        html += self.add_content('    <meta name="robots" content="{}">', self.robots)
        html += '    <meta name="robots" content="max-snippet:150, max-image-preview:large">\n'
        html += self.add_content('    <meta name="creation_date" content="{}">', self.creation_date)
        html += self.add_content('    <meta name="last_modified" content="{}">', self.last_modified)
        html += self.add_content('    <meta name="geo.position" content="{}">', self.geo_lat + "," + self.geo_lng)
        html += self.add_content('    <meta name="ICBM" content="%s">', self.geo_lat + "," + self.geo_lng)
        html += self.add_content('    <meta name="place:location:latitude" content="{}">', self.geo_lat.strip())
        html += self.add_content('    <meta name="place:location:longitude" content="{}">', self.geo_lat.strip())
        html += self.add_content('    <meta name="place:location:altitude" content="{}">', "1")
        html += self.add_content('    <meta name="place:location:accuracy" content="{}">', "100")
        html += self.add_content('    <meta property="business:contact_data:locality" content="{}">', self.geo_city)
        html += self.add_content('    <meta property="business:contact_data:country_name" content="{}">', self.geo_country)
        html += '    <meta name="referrer" content="no-referrer-when-downgrade">' + "\n"
        html += '    <meta name="format-detection" content="telephone=no">' + "\n"

        if not self.canonical_url:
            self.canonical_url = self.get_canonical_link()

        html += '    <link rel="canonical" href="' + self.canonical_url + '">\n'
        html += self.add_content('    <link rel="sitemap" href="{}">', self.sitemap_url)
        html += self.add_content('    <link rel="icon" type="image/png" href="{}">', self.favicon_url)
        html += self.add_content('    <meta name="theme-color" content="{}">', self.theme_color)

        html += '    <meta property="og:type" content="website">\n'
        html += self.add_content('    <meta property="og:site_name" content="{}">', self.site_name)
        html += self.add_content('    <meta property="og:title" content="{}">', self.title)
        html += self.add_content('    <meta property="og:description" content="{}">', self.description)
        html += self.add_content('    <meta property="og:url" content="{}">', self.canonical_url)
        html += self.add_content('    <meta property="og:image" content="{}">', self.fb_image_url)
        if self.fb_image_url:
            html += '    <meta property="og:image:width" content="1200">\n'
            html += '    <meta property="og:image:height" content="630">\n'

        html += '    <meta name="twitter:card" content="summary_large_image">\n'
        html += f'    <meta name="twitter:title" content="{self.title}">\n'
        html += f'    <meta name="twitter:description" content="{self.description}">\n'
        html += f'    <meta name="twitter:image" content="{self.twitter_image_url}">\n'
        if self.twitter_image_url:
            html += '    <meta name="twitter:image:width" content="800">\n'
            html += '    <meta name="twitter:image:height" content="400">\n'

        html += f'    <meta property="og:whatsapp" content="share">\n'
        html += f'    <meta property="og:image:whatsapp" content="{self.whatsapp_image_url}">\n'

        # Add meta tags
        for meta in self.metatags:
            html += f'    <meta name="{meta["name"]}" content="{meta["content"]}">\n'

        # Add CSS links
        for url_css in self.stylesheet_urls:
            html += f'    <link rel="prefetch" href="{url_css}">\n'
            html += f'    <link rel="stylesheet" href="{url_css}">\n'

        # Add JS links
        for url_js in self.script_urls:
            external_url = self.get_external_domain_url(url_js)
            if external_url:
                html += f'    <link rel="dns-prefetch" href="{external_url}">\n'
                html += f'    <script src="{url_js}"></script>\n'

        html += '</head>\n'
        return html