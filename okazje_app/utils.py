import os
import re
from django.conf import settings
from difflib import SequenceMatcher
from django.template.defaultfilters import slugify
import textwrap


def is_similar(a, b):
    ratio = 0
    ratio_real_quick = SequenceMatcher(None, a, b).real_quick_ratio()
    if ratio_real_quick >= 0.8:
        ratio_quick = SequenceMatcher(None, a, b).quick_ratio()
        if ratio_quick >= 0.8:
            ratio = SequenceMatcher(None, a, b).ratio()

    return ratio >= 0.8


def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value


def create_image(input_image, size):
    from PIL import Image
    img_width = size
    img_height = size

    img_white = Image.new('RGB', (img_width, img_height), color=(255, 255, 255, 0))

    img_input = Image.open(input_image)
    img_input_width = img_input.size[0]
    img_input_height = img_input.size[1]
    img_input_ar = img_input_width / img_input_height

    if img_input_width > img_input_height:
        resized = img_input.resize((size, int(size / img_input_ar)), Image.ANTIALIAS)
        img_white.paste(resized, (0, int((size - int(size / img_input_ar)) * 0.5)))
    else:
        resized = img_input.resize((int(size * img_input_ar), size), Image.ANTIALIAS)
        img_white.paste(resized, (int((size - int(size * img_input_ar)) * 0.5), 0))

    from io import BytesIO
    output = BytesIO()
    img_white.save(output, 'webp', quality=90)
    contents = output.getvalue()
    output.close()

    return contents


def create_image_from_text(text):
    from PIL import Image, ImageDraw, ImageFont
    from string import ascii_letters

    font_path = os.path.join(settings.SITE_ROOT, 'font.ttf')

    img_width = 1200
    img_height = 630

    img = Image.new('RGB', (img_width, img_height), color=(255, 250, 240))

    # print(f'font path: {font_path}')

    font_size = 70
    text_height = 99999999

    while text_height > img_height:
        font_size = font_size - 4
        fnt = ImageFont.truetype(font_path, font_size)
        # fnt = ImageFont.load_default()
        font_height = fnt.getsize('aaXX')[1]

        avg_char_width = sum(fnt.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

        body = text
        body = '\n'.join(
            ['\n'.join(
                textwrap.wrap(line, img_width / avg_char_width, break_long_words=False, replace_whitespace=False))
                for line in body.splitlines() if line.strip() != ''])

        lines_number = body.count('\n') + 1
        text_height = lines_number * (font_height * 1.5)

    d = ImageDraw.Draw(img)
    d.text((50, img_height * 0.5), body, font=fnt, fill=(74, 74, 74), anchor='lm',
           spacing=font_height * 0.5, align='left')

    img.paste(Image.open(os.path.join(settings.SITE_ROOT, 'logo.png')), (img_width - 115, 15))

    from io import BytesIO
    output = BytesIO()
    img.save(output, 'PNG')
    contents = output.getvalue()
    output.close()

    return contents
