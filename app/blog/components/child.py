from django_unicorn.components import UnicornView


class ChildView(UnicornView):
    def child_click(self):
        print("child_click")
        self.parent.sample_value = "child"
        # Parent's value doesn't change in template
        print(self.parent.sample_value)
