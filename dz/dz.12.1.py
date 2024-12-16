import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned_text = re.sub(r'<[^>]*>', '', html)


    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    cleaned_text = '\n'.join(non_empty_lines)

    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(cleaned_text)

delete_html_tags('draft.html', 'cleaned.txt')
