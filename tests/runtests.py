# coding: utf8
import os
from unittest import TestCase
from pydf import generate_pdf, get_version, get_help, get_extended_help

import sys
if sys.version_info[0] == 3:
    def byteify(s):
        return bytes(s, encoding='utf8')
else:
    def byteify(s):
        return s


class PydfTestCase(TestCase):
    def test_generate_pdf_with_html(self):
        pdf_content = generate_pdf('<html><body>Is this thing on?</body></html>')
        assert pdf_content[:4] == byteify('%PDF')

    def test_generate_pdf_with_url(self):
        pdf_content = generate_pdf('http://google.com')
        assert pdf_content[:4] == byteify('%PDF')

    def test_unicode(self):
        pdf_content = generate_pdf(u'<html><body>Schrödinger</body></html>')
        assert pdf_content[:4] == byteify('%PDF')

    def test_extra_arguments(self):
        pdf_content = generate_pdf(
            '<html><body>testing</body></html>',
            quiet=False,
            grayscale=True,
            lowquality=True,
            margin_bottom='20mm',
            margin_left='20mm',
            margin_right='20mm',
            margin_top='20mm',
            orientation='Landscape',
            page_height=None,
            page_width=None,
            page_size='Letter',
            image_dpi='300',
            image_quality='70',
        )
        assert pdf_content[:4] == byteify('%PDF')

    def test_custom_size(self):
        pdf_content = generate_pdf(
            '<html><body>testing</body></html>',
            page_height='50mm',
            page_width='50mm',
        )
        assert pdf_content[:4] == byteify('%PDF')

    def test_extra_kwargs(self):
        pdf_content = generate_pdf(
            '<html><body>testing</body></html>',
            header_right='Page [page] of [toPage]'
        )
        assert pdf_content[:4] == byteify('%PDF')

    def test_wrong_path(self):
        os.environ['WKHTMLTOPDF_CMD'] = 'foo bar'
        self.assertRaises(IOError, get_help)
        del os.environ['WKHTMLTOPDF_CMD']

    def test_no_arguments(self):
        self.assertRaises(TypeError, generate_pdf)

    def test_bad_arguments(self):
        self.assertRaises(IOError, generate_pdf, 'www.')

    def test_get_version(self):
        print(get_version())

    def test_get_help(self):
        get_help()

    def test_get_extended_help(self):
        get_extended_help()
