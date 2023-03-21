from flask import Flask, render_template, Markup
from src.head_generator import head_generator

app = Flask(__name__, template_folder='templates')


def generate_head() -> object:
    head = head_generator()
    head.set_language("fr")
    head.set_viewport("width=device-width, initial-scale=1")
    head.set_title("Page Title - Important Keywords | Brand Name")
    head.set_description("Relevant description of the page in less than 160 characters")
    head.set_keywords("Important keywords separated by commas")
    head.set_author("Author or company name")
    head.set_canonical_url("https://yourdomain.tld")
    head.set_robots("noindex, nofollow")
    head.set_creation_date("2023-03-20")
    head.set_last_modified("2023-03-21")
    head.set_geo_lat("14.610360")
    head.set_geo_lng("-61.073381")
    head.set_geo_city("Pilot-River")
    head.set_geo_country("Guadeloupe")
    head.set_sitemap_url("https://yourdomain.tld/sitemap.xml")
    head.set_favicon_url("https://yourdomain.tld/favicon.png")
    head.set_theme_color("#ffffff")
    head.set_site_name("Company name")
    head.set_fb_image_url("https://yourdomain.tld/assets/img/fb-share-1200-630.png")
    head.set_twitter_image_url("https://yourdomain.tld/assets/img/twitter-share-800-400.png")
    head.set_whatsapp_image_url("https://yourdomain.tld/assets/img/whatsapp-share-300-200.png")
    head.add_stylesheet_urls("https://yourdomain.tld/assets/css/style.css")
    head.add_script_urls("https://yourdomain.tld/assets/js/script.js")
    head.add_script_urls("https://cdn.example.com/js/plugin.js")
    header = head.render()
    return Markup(header)


@app.route('/')
def index():
    head = generate_head()
    return render_template('index.html', head=head)


if __name__ == '__main__':
    app.run(debug=True)
