import bleach
from markdown import markdown


html = '<img style="max-width:30%;" src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1520347690777&amp;di=6a11fa8abc8d1a8bb8e3473ab1f2e56b&amp;imgtype=0&amp;src=http%3A%2F%2Fimgsrc.baidu.com%2Fimgad%2Fpic%2Fitem%2F32fa828ba61ea8d3d8d6c33f9c0a304e251f5810.jpg">'

allow_tags = ['img']
result_markdown = markdown(html, output_format='html')
attrs = {
    '*': ['color', 'style'],
    'img': ['href', 'src'],
    'p': ['href', 'src'],
}
result_clean = bleach.clean(result_markdown, tags=allow_tags, attributes=attrs, styles=['color', 'max-width'], strip=True)
target = bleach.linkify(result_clean)

print('markdown:%s' % result_markdown)
print('clean:%s' % result_clean)
print('linkfy:%s' % target)


