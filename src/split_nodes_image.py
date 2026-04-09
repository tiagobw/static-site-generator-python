from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        current_text = old_node.text
        images = extract_markdown_images(current_text)
        for image in images:
            image_alt, image_link = image
            sections = current_text.split(f"![{image_alt}]({image_link})", 1)
            text_left = sections[0]
            text_right = sections[1]
            if text_left != "":
                result.append(TextNode(text_left, TextType.TEXT))
            result.append(TextNode(image_alt, TextType.IMAGE, image_link))
            current_text = text_right
        if current_text != "":
            result.append(TextNode(current_text, TextType.TEXT))
    return result
