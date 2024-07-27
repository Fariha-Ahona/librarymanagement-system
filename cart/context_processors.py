from .cart import Cart

#here is the context processor so our cart can work on all oages of website
def cart(request):
    #return the default data from our cart
    return{'cart': Cart(request)}
