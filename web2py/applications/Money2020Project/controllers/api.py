@request.restful()
def performTransaction():
    def GET():
        return 'Hello World from performTransaction GET'
    def POST(*args,**vars):
        return 'Hello World from performTransaction POST'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)

# example 
@request.restful()
def testEndpoint():
    def GET():
        return 'Hello World from testEndpoint GET'
    def POST(*args,**vars):
        return 'Hello World from testEndpoint POST'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)
