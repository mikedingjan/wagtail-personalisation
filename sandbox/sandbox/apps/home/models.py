from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore import blocks, fields
from wagtail.wagtailcore.models import Page

from wagtail_personalisation.blocks import (PersonalisedCharBlock,
    PersonalisedImageChooserBlock, PersonalisedRichTextBlock,
    PersonalisedStructBlock, PersonalisedTextBlock)
from wagtail_personalisation.models import PersonalisablePageMixin


class HomePage(Page, PersonalisablePageMixin):
    pass


class PersonalisedFieldsPage(Page):
    body = fields.StreamField([
        ('personalised_block', PersonalisedStructBlock([
            ('heading', blocks.CharBlock()),
            ('paragraph', blocks.RichTextBlock())
        ], render_fields=['heading', 'paragraph'])),
        ('personalised_block_template', PersonalisedStructBlock([
            ('heading', blocks.CharBlock()),
            ('paragraph', blocks.RichTextBlock())
        ], template='blocks/personalised_block_template.html', label=_('Block with template'))),
        ('personalised_rich_text_block', PersonalisedRichTextBlock()),
        ('personalised_image', PersonalisedImageChooserBlock()),
        ('personalised_char', PersonalisedCharBlock()),
        ('personalised_text', PersonalisedTextBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
