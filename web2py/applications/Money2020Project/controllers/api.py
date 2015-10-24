@request.restful()
def performTransaction():
    def GET():
        return 'Hello World from performTransaction GET'
    def POST(*args,**vars):
        import simplify
		simplify.public_key = "sbpb_MzZiNTQ2MTAtMGY2ZS00NGI4LWEzNzEtYjQyMTU4NzhiM2Vj"
		simplify.private_key = "WuHzM3OXNN5eO1kWM8dRJtYNzgfbF6dtA+w8FElar/N5YFFQL0ODSXAOkNtXTToq"
		payment = simplify.Payment.create({
       "card" : {
            "number": "5555555555554444",
            "expMonth": 11,
            "expYear": 15,
            "cvc": "123"
        },
        "amount" : "1000",
        "description" : "prod description",
        "currency" : "USD"
})
if payment.paymentStatus == 'APPROVED':
    print "Payment approved"
		
		return 'Hello World from performTransaction POST'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)



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

