from graphviz import Digraph


def create_er_diagram():
    dot = Digraph(format='png')
    dot.attr(dpi='300')

    # Определение сущностей
    dot.node('Customer', 'Customer\n(Customer_ID, Name, Email, Phone, Address)', shape='box')
    dot.node('Book', 'Book\n(ISBN, Title, Year, Price, Publisher_ID)', shape='box')
    dot.node('Author', 'Author\n(Author_ID, Name, Address, Website)', shape='box')
    dot.node('Publisher', 'Publisher\n(Publisher_ID, Name, Address, Phone, Website)', shape='box')
    dot.node('Warehouse', 'Warehouse\n(Warehouse_ID, Address, Phone)', shape='box')
    dot.node('Stock', 'Stock\n(Warehouse_ID, ISBN, Quantity)', shape='box')
    dot.node('ShoppingCart', 'ShoppingCart\n(Cart_ID, Customer_ID)', shape='box')
    dot.node('CartItem', 'CartItem\n(Cart_ID, ISBN, Quantity)', shape='box')
    dot.node('Order', 'Order\n(Order_ID, Customer_ID, Date, TotalPrice, PaymentInfo, ShippingAddress)', shape='box')
    dot.node('OrderItem', 'OrderItem\n(Order_ID, ISBN, Quantity, Price)', shape='box')

    # Определение связей
    dot.edge('Customer', 'ShoppingCart', label='1 has N')
    dot.edge('ShoppingCart', 'CartItem', label='1 contains N')
    dot.edge('Book', 'CartItem', label='1 appears in N')
    dot.edge('Customer', 'Order', label='1 places N')
    dot.edge('Order', 'OrderItem', label='1 contains N')
    dot.edge('Book', 'OrderItem', label='1 appears in N')
    dot.edge('Book', 'Stock', label='1 stored in N')
    dot.edge('Warehouse', 'Stock', label='1 has N')
    dot.edge('Book', 'Author', label='N written by M')
    dot.edge('Book', 'Publisher', label='N published by 1')

    return dot


# Создание и рендер ER-диаграммы
er_diagram = create_er_diagram()
er_diagram.render('er_diagram_martin', format='png', cleanup=True)
