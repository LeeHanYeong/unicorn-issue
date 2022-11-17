from django_unicorn.components import UnicornView


class SampleView(UnicornView):
    sample_value = "default"

    def sample(self):
        self.sample_value = "sample"

    def rendered(self, html):
        print(self.children)

    def updated(self, name, value):
        # updated not called
        print("updated", name, value)

    def set_sample(self, value):
        self.sample_value = value
        print(f"parent.set_sample({value})")

        # self.children is Empty
        # (All children present at the time of rendering disappear)
        print(self.children)
