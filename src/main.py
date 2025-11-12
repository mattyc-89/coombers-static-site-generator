from textnode import TextNode, TextType

def main():
    node = TextNode("This is anchor text", TextType.LINK, "https://example.com")
    print(node)

if __name__ == "__main__":   
    main()    
