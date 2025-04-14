from openai import OpenAI
from SeePlanAct.src.seeplanact import run_agent_sync

def run(input: dict[str, dict], **kwargs) -> dict[str, str]:

    assert 'model_name' in kwargs, 'model_name is required'
    client = OpenAI()

    # Store the results
    agent_output = {}

    config_path = "config/demo_mode.toml"

    # Iterate through the tasks
    for task_id, task_info in input.items():
        print(f'Generating {task_id}...')

        instruction = task_info.get("task")
        config_override = {"default_task": instruction}\

        result = run_agent_sync(config_path, config_override=config_override, model_name=kwargs['model_name'])

        print(f"Response for {task_id}: {result}")
        agent_output[task_id] = result

    return agent_output