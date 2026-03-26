from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception(
                "Invalid Markdown syntax: It's missing a closing delimiter!"
            )

        splitted_text = old_node.text.split(delimiter)
        for index, text in enumerate(splitted_text):
            if text == "":
                continue

            if index % 2 != 0:
                result.append(TextNode(text, text_type))
            else:
                result.append(TextNode(text, TextType.TEXT))

    return result
