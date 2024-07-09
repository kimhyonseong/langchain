from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, model_validator

chat = ChatOpenAI()

class Smartphone(BaseModel):
    model_config = {"extra": "forbid"}
    release_date: str = Field(description="스마트폰 출시일")
    screen_inches: float = Field(description="스마트폰의 화면 크기(인치)")
    os_installed: str = Field(description="스마트폰에 설치된 OS")
    model_name: str = Field(description="스마트폰 모델명")

    @model_validator(mode='before')
    def validate_screen_inches(cls, values):
        if 'screen_inches' in values and values['screen_inches'] <= 0:
            raise ValueError("Screen inches  must be a positive number")
        return values
    
parser = PydanticOutputParser(pydantic_object=Smartphone)

result = chat([
    HumanMessage(content="안드로이드 스마트폰 1개를 꼽아주세요."),
    HumanMessage(content=parser.get_format_instructions())
])

parser_result = parser.parse(result.content)

print(f"모델명: {parser_result.model_name}")
print(f"화면크기: {parser_result.screen_inches}")
print(f"설치된 OS: {parser_result.os_installed}")
print(f"출시일: {parser_result.release_date}")