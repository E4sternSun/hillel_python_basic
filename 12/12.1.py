def delete_html_tags(html_file: str) -> None:
    """
    Очищає HTML-файл від тегів і записує результат у файл.

    :param html_file: Ім'я вихідного HTML-файлу.
    """
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    cleaned_text = ''
    inside_tag = False
    for char in html_content:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text += char

    lines = cleaned_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]
    final_text = '\n'.join(non_empty_lines)

    with open('cleaned.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(final_text)

delete_html_tags("draft.html")