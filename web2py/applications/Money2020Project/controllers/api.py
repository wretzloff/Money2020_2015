@request.restful()
def testEndpoint():
    def GET():
        import json
    	'''
        import simplify
        simplify.public_key = "sbpb_MzZiNTQ2MTAtMGY2ZS00NGI4LWEzNzEtYjQyMTU4NzhiM2Vj"
        simplify.private_key = "WuHzM3OXNN5eO1kWM8dRJtYNzgfbF6dtA+w8FElar/N5YFFQL0ODSXAOkNtXTToq"
        '''
		#Required parameter: 'merchantID'
        #Contains an ID that identifies who is being paid (Costco, Walmart, etc.)
        merchantID = 1#request.post_vars['merchantID']

		#Required parameter: 'items'
		#Contains a JSON string representing an array of items that were purchased.
        itemsJson = json.loads('{"items": [{"name": "tomato","price": "2.93"},{"name": "tooth brush","price": "9.99"}]}')#request.post_vars['items']

		#Required parameter: 'cardNumber'
        #
        cardNumber = "5555555555554444"#request.post_vars['cardNumber']

		#Required parameter: 'cardExpMonth'
        #
        cardExpMonth = 11#request.post_vars['cardExpMonth']

		#Required parameter: 'cardExpYear'
        #
        cardExpYear = 15#request.post_vars['cardExpYear']

		#Required parameter: 'cardCvc'
        #
        cardCvc = "123"#request.post_vars['cardCvc']

		#Sum the price of all the items
        sum = 0.00
        for item in itemsJson['items']:
            sum = sum + float(item['price'])
        print 'Sum of items: ' + str(sum)
        
        '''
		#Charge the user's card. We will receive this payment.
        payment = simplify.Payment.create({
			"card" : {
            "number": cardNumber,
            "expMonth": cardExpMonth,
            "expYear": cardExpYear,
            "cvc": cardCvc
        },
        	"amount" : sum,
        	"description" : "Costco",
        	"currency" : "USD"
		})
        if payment.paymentStatus == 'APPROVED':
			print "Payment approved"
        '''
		#Send money to Merchant
		#TODO

		#Save receipt to database
		#TODO
        return 'Hello World from testEndpoint GET'
    def POST(*args,**vars):
        return 'Hello World from testEndpoint POST'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)
