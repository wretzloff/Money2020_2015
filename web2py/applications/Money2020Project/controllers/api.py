import json
import simplify

@request.restful()
def processTransaction():
    def GET():
        return 'process GET'
    def POST(*args,**vars):
        simplify.public_key = "sbpb_MzZiNTQ2MTAtMGY2ZS00NGI4LWEzNzEtYjQyMTU4NzhiM2Vj"
        simplify.private_key = "WuHzM3OXNN5eO1kWM8dRJtYNzgfbF6dtA+w8FElar/N5YFFQL0ODSXAOkNtXTToq"
        
		#Required parameter: 'merchantID'
        #Contains an ID that identifies who is being paid (Costco, Walmart, etc.)
        #merchantID = request.post_vars['merchantID']
        merchantID = 1

		#Required parameter: 'items'
		#Contains a JSON string representing an array of items that were purchased.
        #itemsJson = request.post_vars['items']
        itemsJson = json.loads('{"items": [{"name": "tomato","price": "2.93"},{"name": "tooth brush","price": "9.99"}]}')

		#Required parameter: 'cardNumber'
        #cardNumber = request.post_vars['cardNumber']
        cardNumber = "5555555555554444"

		#Required parameter: 'cardExpMonth'
        #cardExpMonth = request.post_vars['cardExpMonth']
        cardExpMonth = 11

		#Required parameter: 'cardExpYear'
        #cardExpYear = request.post_vars['cardExpYear']
        cardExpYear = 15

		#Required parameter: 'cardCvc'
        #cardCvc = request.post_vars['cardCvc']
        cardCvc = "123"

		#sumItemPrices the price of all the items
        sumItemPrices = 0.00
        for item in itemsJson['items']:
            sumItemPrices = sumItemPrices + float(item['price'])
        sumItemPrices = sumItemPrices*100
        print 'sumItemPrices of items: ' + str(sumItemPrices)
        
		#Charge the user's card. We will receive this payment.
        payment = simplify.Payment.create({
        	"card" : {
            "number": cardNumber,
            "expMonth": cardExpMonth,
            "expYear": cardExpYear,
            "cvc": cardCvc
        },
        "amount" : sumItemPrices,
        "description" : "Costco",
        "currency" : "USD"
        })
                
		#TODO: Now that we've been paid, we need to pay that money forward to  the merchant.
		#TODO: This transaction is complete. Save important info to database for analytics.
        
        if payment.paymentStatus == 'APPROVED':
			return 'Payment approved: ' + str(sumItemPrices)
        else:
            return 'Payment declined.'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)

@request.restful()
def getItemInfo():
    def GET(itemID):
        print itemID
        itemName = None
        itemPrice = None
        if itemID == '038000635502':
            itemName = 'Kellogs Special K Original Toasted Rice Cereal'
            itemPrice = '3.25'
        elif itemID == '03400704':
            itemName = 'Ice Breakers Mints'
            itemPrice = '2.35'
        elif itemID == '03400704':
            itemName = 'KIND Fruit & Nut Delight'
            itemPrice = '1.25'
        elif itemID == '04913207':
            itemName = 'Sprite'
            itemPrice = '0.99'
        elif itemID == '04963406':
            itemName = 'Coca-Cola'
            itemPrice = '0.99'

        elif itemID == '602652170041':
            itemName = 'Kind Fruit & Nut Delight'
            itemPrice = '1.59'
        elif itemID == '722252100900':
            itemName = 'Clif Bar Chocolate Chip'
            itemPrice = '2.79'
        elif itemID == '04913207':
            itemName = 'Sprite 12 oz'
            itemPrice = '.99'
        elif itemID == '04963406':
            itemName = 'Coca Cola 12 oz'
            itemPrice = '.99'
        elif itemID == '03400704':
            itemName = 'Ice Breakers Mints Coolmint'
            itemPrice = '.89'
        else:
            itemName = 'unknown'
            itemPrice = 'unknown'
        returnString = "{\"itemID\":\"" + itemID + "\",\"itemName\":\"" + itemName + "\",\"itemPrice\":\"" + itemPrice + "\"}"
        return returnString
    def POST(*args,**vars):
        return 'Hello World from getItemInfo POST'
    def PUT(*args,**vars):
        return ''
    def DELETE():
        return ''
    return dict(GET=GET, POST=POST, PUT=PUT, DELETE=DELETE)
