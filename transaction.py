class Transaction:

    def __init__(self, transaction_type, amount, date, account_no, receiver_account_no):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__date = date
        self.__account_no = account_no
        self.__receiver_account_no = receiver_account_no

    def get_transaction_type(self):
        return self.__transaction_type

    def get_account_no(self):
        return self.__account_no

    def set_account_no(self):
        self.__account_no = self.__receiver_account_no

    def get_amount(self):
        return self.__amount

    def get_receiver_account_no(self):
        return self.__receiver_account_no

    def print_info(self):
        transaction_type = " "
        if self.__transaction_type == 1:
            transaction_type = "DEPOSIT"
        elif self.__transaction_type == 2:
            transaction_type = "WITHDRAW"
        elif self.__transaction_type == 3:
            transaction_type = "TRANSFER"

        print("{:<20}{:>10}{:>20}".format(self.__date, self.__amount, transaction_type))