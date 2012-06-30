from rollyourown import seo

class MyMetadata(seo.Metadata):
    title       = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords    = seo.KeywordTag()
    # Adding some fields for facebook (opengraph)
    og_title    = seo.MetaTag(name="og:title", populate_from="title", verbose_name="facebook title")
    og_description = seo.MetaTag(name="og:description", populate_from="description", verbose_name='facebook description')
    class Meta:
        seo_models = ('comics',)
