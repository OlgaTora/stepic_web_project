def wsgi_application(environ, start_response): 
# бизнес-логика
    status = '200 OK'
    headers = [ ('Content-Type', 'text/plain')б  ('Content-Length', str(len(data)))]
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')] start_response(status, headers )
    return body.encode('utf-8')


