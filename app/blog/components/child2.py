from django_unicorn.components import UnicornView


class Child2View(UnicornView):
    def child2_click(self):
        print("child2_click")
        self.parent.set_sample("child2")
        # Parent's value doesn't change in template
        print(self.parent.sample_value)
