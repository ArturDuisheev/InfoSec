import uuid

from pytils.translit import slugify


def unique_slugify(field):
    unique_slug = slugify(field)
    unique_slug = f'{unique_slug}-{uuid.uuid4().hex[:8]}'

    return unique_slug
