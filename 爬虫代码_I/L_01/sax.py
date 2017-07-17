''' Parse XML using SAX '''
# coding:utf-8

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    ''' SAX parser '''
    def __init__(self):
        self.CurrentData = ''
        self.type = ''
        self.format = ''
        self.year = ''
        self.rating = ''
        self.stars = ''
        self.description = ''

    # Processe element start
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'movie':
            print('*****Movie*****')
            title = attributes['title']
            print('\tTitle:%s' % title)

    # Processe element end
    def endElement(self, tag):
        if self.CurrentData == 'type':
            print('\tType:%s' % self.type)
        elif self.CurrentData == 'format':
            print('\tFormat:%s' % self.format)
        elif self.CurrentData == 'year':
            print('\tYear:%s' % self.year)
        elif self.CurrentData == 'rating':
            print('\tRating:%s' % self.rating)
        elif self.CurrentData == 'stars':
            print('\tStars:%s' % self.stars)
        elif self.CurrentData == 'description':
            print('\tDescription:%s' % self.description)
        self.CurrentData = ''

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == 'type':
            self.type = content
        elif self.CurrentData == 'format':
            self.format = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'rating':
            self.rating = content
        elif self.CurrentData == 'stars':
            self.stars = content
        elif self.CurrentData == 'description':
            self.description = content
  
if __name__ == '__main__':
   PARSER = xml.sax.make_parser()
   PARSER.setFeature(xml.sax.handler.feature_namespaces, 0)
   PARSER.setContentHandler(MovieHandler())
   PARSER.parse('sample.xml')