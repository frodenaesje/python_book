# file: sc_11_05_AccountE_with_exception_detail.py
# demonstrates the interaction between the Exception class
# and the BankAccountError class
class BankAccountError(Exception):
    def __init__(self, message, account_number=None, balance=None):
        print("1. BankAccountError.__init__ receives:")
        print(f"   message = {message!r}")

        print("\n2. super().__init__(message) calls Exception.__init__")
        super().__init__(message)

        print("   After the call:")
        print(f"   self.args = {self.args!r}")
        print(f"   type(self.args) = {type(self.args).__name__}")

        self._account_number = account_number
        self._balance = balance

    @property
    def message(self):
        print("\n4. The message property reads self.args")
        print(f"   self.args = {self.args!r}")
        return self.args[0] if self.args else ""


error = BankAccountError("Balance cannot be negative", 456, 1000)

print("\n3. Read the inherited args attribute directly:")
print(f"   error.args = {error.args!r}") # error.args!r same as repr(error.args)

print("\n   Access error.message:")
text = error.message
print(f"   Returned value: {text!r}")