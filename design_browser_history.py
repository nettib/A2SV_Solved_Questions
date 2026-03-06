class Link:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Link(homepage)

    def visit(self, url: str) -> None:
        new_link = Link(url)
        if not self.homepage:
            self.homepage = new_link
        
        curr = self.homepage
        curr.next = new_link
        new_link.prev = curr
        self.homepage = new_link

    def back(self, steps: int) -> str:
        i = 0

        while i != steps and self.homepage.prev:
            self.homepage = self.homepage.prev
            i += 1
        
        return self.homepage.url

    def forward(self, steps: int) -> str:
        i = 0

        while i != steps and self.homepage.next:
            self.homepage = self.homepage.next
            i += 1
        
        return self.homepage.url

# l - g - f - y        
# l - g - f - y

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
