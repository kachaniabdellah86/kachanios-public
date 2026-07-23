from src.models import AgentRequest, AgentResult
from src.router import route_message


def process_request(request: AgentRequest) -> AgentResult:
    domain = route_message(request.message)
    response = (
        f"I classified this request as {domain.replace('_', ' ')} "
        "and prepared a structured next step."
    )
    return AgentResult(domain=domain, response=response)
