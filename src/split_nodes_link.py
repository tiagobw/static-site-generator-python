from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        current_text = old_node.text
        links = extract_markdown_links(current_text)
        for link in links:
            link_text, link_url = link
            sections = current_text.split(f"[{link_text}]({link_url})", 1)
            text_left = sections[0]
            text_right = sections[1]
            if text_left != "":
                result.append(TextNode(text_left, TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, link_url))
            current_text = text_right
        if current_text != "":
            result.append(TextNode(current_text, TextType.TEXT))
    return result
