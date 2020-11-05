class Shop1:

    total_sales = 0

    def __init__(self, shop_name, sales):
        self.shop_name = shop_name
        self.sales = sales
        self.__class__.total_sales += sales

    def make_sales(self, sales):
        self.sales += sales
        self.__class__.total_sales += sales

    @classmethod
    def get_total_sales(cls):
        if cls.total_sales < 1000:
            return 'Продажи идут плохо', cls.total_sales
        return 'Продажи идут хорошо', cls.total_sales


print(Shop1.get_total_sales())