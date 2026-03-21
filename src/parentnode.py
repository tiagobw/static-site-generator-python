from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            raise ValueError("All parent nodes must have children.")
        children_html = []
        for child in self.children:
            children_html.append(child.to_html())
        return (
            f"<{self.tag}{self.props_to_html()}>{"".join(children_html)}</{self.tag}>"
        )

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
