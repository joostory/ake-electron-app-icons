#!/usr/bin/env python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from PIL import Image, ImageDraw, ImageFont
import os


class IconMaker:
    def __init__(self, source, output):
        self.source = source
        self.output = output
        self.output_icons = '{}/icons'.format(output)
        self.image = Image.open(source)

    def make_all(self):
        self.prepare_output()
        self.make_ico()
        self.make_icons()
        self.make_icns()

    def prepare_output(self):
        print('prepare_output:{}'.format(self.output))
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        if not os.path.exists(self.output_icons):
            os.makedirs(self.output_icons)

    def make_ico(self):
        img = self.image.resize((256, 256), Image.ANTIALIAS)
        img.save('{0}/icon.ico'.format(self.output), 'ICO')

    def make_icons(self):
        for size in [16, 24, 32, 48, 64, 96, 128, 256, 512]:
            img = self.image.resize((size, size), Image.ANTIALIAS)
            img.save('{0}/{1}x{1}.png'.format(self.output_icons, size), 'png')

    def make_icns(self):
        os.system('/usr/bin/png2icns {0}/icon.icns {1}/16x16.png {1}/32x32.png {1}/128x128.png {1}/256x256.png {1}/512x512.png'.format(self.output, self.output_icons))
        pass

def main():
    usage = 'usage: %prog [options] source_image'
    parser = OptionParser(usage)
    parser.add_option('--output', type='string', default='output', help='output dir')

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error('no source')

    iconMaker = IconMaker(
        source = args[0],
        output = options.output
    )
    iconMaker.make_all()


if __name__ == '__main__':
    main()