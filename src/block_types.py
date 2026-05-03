from enum import Enum


class BlockType(Enum):
	PARAGRAPH='paragraph'
	HEADING='heading'
	CODE='code'
	QUOTE='quote'
	UNORDERED_LIST='unordered list'
	ORDERED_LIST='ordered list'
	

def block_to_block_type(block: str) -> BlockType:
	