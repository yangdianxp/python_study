class Foo:
    def get_bar(self):
        return "laowang"

    BAR = property(get_bar)

obj = Foo()
result = obj.BAR
print(result)


