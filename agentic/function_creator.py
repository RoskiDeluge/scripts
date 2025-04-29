
from swarm import Agent
from swarm.repl import run_demo_loop

agent = Agent(
    name="Bootstrap",
    instructions="",
    functions=[],
    )


def parse_function(code_str):
    namespace = {}
    exec(code_str, namespace)
    fn_name = next(k for k in namespace if not k.startswith("__"))
    return namespace[fn_name]


def add_tool(python_implementation: str):
    function_obj = parse_function(python_implementation)
    agent.functions.append(function_obj)
    return "success"

agent.functions = [add_tool]

run_demo_loop(agent)
