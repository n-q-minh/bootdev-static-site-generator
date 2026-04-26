import re


def extract_markdown_links(string: str) -> list[tuple[str, str]]:
    pattern = r'\[(?P<text>[^\(]*)\]\((?P<link>[^\[]*)\)'
    '''
    r = re.compile(pattern)
    matches = [m.groupdict() for m in r.finditer(text)]
    '''
    result = re.findall(pattern, string)
    return result


def extract_markdown_images(string: str) -> list[tuple[str, str]]:
    pattern = r'!\[(?P<text>[^\(]*)\]\((?P<link>[^\[]*)\)'
    result = re.findall(pattern, string)
    return result