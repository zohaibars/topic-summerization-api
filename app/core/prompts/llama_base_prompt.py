import logging

class llama_prompt_builder:
    def __init__(
        self,
        system,
        user_prompt
    ):
        self.system = system
        self.user_prompt = user_prompt
    
    def create_llama_prompt(self):
        prompt = ""
        base_prompt = ( 
            "<|begin_of_text|>"  # Start of prompt
            "<|start_header_id|>system<|end_header_id|>\n\n"  #  header - system
            f"{self.system}"  # system prompt
            "<|eot_id|>" # end of turn
            "<|start_header_id|>user<|end_header_id|>\n\n" # header - user
            f"{self.user_prompt}" 
            "<|eot_id|>" # end of turn
            "<|start_header_id|>assistant<|end_header_id|>\n\n" # header - assistant    
        )
        return prompt