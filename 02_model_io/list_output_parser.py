from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage

output_parser = CommaSeparatedListOutputParser()

print(output_parser.get_format_instructions())

chat = ChatOpenAI(model="gpt-3.5-turbo")

result = chat(
    [
        HumanMessage(content="애플이 개발한 대표적인 제품 3개를 알려주세요"),
        HumanMessage(content=output_parser.get_format_instructions()),
    ]
)

print(result)

output = output_parser.parse(result.content)

for item in output:
    print("대표 상품 => " + item)