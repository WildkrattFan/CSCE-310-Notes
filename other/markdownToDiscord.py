import re

def convert_markdown_to_discord(markdown_text):
    # Convert headers
    for i in range(6, 0, -1):
        markdown_text = re.sub(r'^(#{' + str(i) + r'}) (.*)', r'{"*" * (6 - i) + r" } \2', markdown_text, flags=re.MULTILINE)

    # Convert bold text
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', markdown_text)  # **text** => **text**
    markdown_text = re.sub(r'__(.*?)__', r'**\1**', markdown_text)  # __text__ => **text**

    # Convert italic text
    markdown_text = re.sub(r'\*(.*?)\*', r'*\1*', markdown_text)  # *text* => *text*
    markdown_text = re.sub(r'_(.*?)_', r'*\1*', markdown_text)  # _text_ => *text*

    # Convert links
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'[\1](\2)', markdown_text)  # [text](url) => [text](url)

    # Convert unordered lists
    markdown_text = re.sub(r'^\* (.+)', r'- \1', markdown_text, flags=re.MULTILINE)  # * item => - item
    markdown_text = re.sub(r'^\+ (.+)', r'- \1', markdown_text, flags=re.MULTILINE)  # + item => - item
    markdown_text = re.sub(r'^\- (.+)', r'- \1', markdown_text, flags=re.MULTILINE)  # - item => - item

    # Convert ordered lists
    markdown_text = re.sub(r'^\d+\. (.+)', r'1. \1', markdown_text, flags=re.MULTILINE)  # 1. item => 1. item

    return markdown_text

def main():
    # Load the Markdown file
    input_filename = 'README.md'  # Change this to your markdown file path
    with open(input_filename, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Convert to Discord text
    discord_text = convert_markdown_to_discord(markdown_content)

    # Output the result
    print(discord_text)

    # Optionally, save to a file
    output_filename = 'output.txt'  # Change this to your desired output file path
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(discord_text)

if __name__ == '__main__':
    main()
