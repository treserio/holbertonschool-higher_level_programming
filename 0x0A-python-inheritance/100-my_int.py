class MyInt(int):
    def __init__(self, val):
        self.val = val

    def __eq__(self, obj):
        return self.val != obj

    def __ne__(self, obj):
        return self.val == obj
