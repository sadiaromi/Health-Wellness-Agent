class Tool:
    name: str
    description: str

    def run(self, input_data, context):
        raise NotImplementedError("Tool must implement a `run()` method.")
