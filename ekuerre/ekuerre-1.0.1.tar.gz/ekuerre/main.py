from io import BytesIO
from urlparse import parse_qs
from StringIO import StringIO
import qrcode
import barcode

barcode_types = set([u'code128'])

def application(environ, start_response):
    path = environ['PATH_INFO']
    if path.startswith('/qr.png'):
        params = parse_qs(environ['QUERY_STRING'])
        data = params.get('data', [None])[0]
        code = qrcode.QRCode()
        code.add_data(data)
        code.make(fit=True)
        image = code.make_image()
        the_bytes = BytesIO()
        image.save(the_bytes)

        headers = [
            ('Content-Type', 'image/png'),
        ]
        start_response('200 OK', headers)
        return [the_bytes.getvalue()]

    elif path.startswith('/barcode.png'):
        params = parse_qs(environ['QUERY_STRING'])
        kind = params.get('type', [None])[0]
        data = params.get('data', [None])[0]
        fmt  = params.get('format', ['code128'])[0]
        module_height = float(params.get('module_height', [64])[0])
        text_distance = int(params.get('text_distance', [1])[0])

        if kind not in barcode_types:
            headers = [
                ('Content-Type', 'text/plain'),
            ]
            start_response('404 Not Found', headers)
            return [b'wrong type']

        woptions = barcode.base.Barcode.default_writer_options

        if module_height is not None:
            woptions['module_height'] = module_height

        if text_distance is not None:
            woptions['text_distance'] = text_distance

        output = StringIO()
        aja = barcode.generate(kind, data,
            output=output,
            writer=barcode.writer.ImageWriter(),
            writer_options=woptions,
        )

        headers = [
            ('Content-Type', 'image/png'),
        ]
        start_response('200 OK', headers)
        return [output.getvalue()]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 32491, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("stopped")