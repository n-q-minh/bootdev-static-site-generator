def markdown_to_blocks(string: str) -> list[str]:
    blocks = [sblock for block in string.split('\n\n') if (sblock := block.strip())]
    return blocks
