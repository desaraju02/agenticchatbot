# import json
# import yaml
# from pathlib import Path
# from typing import Any, Dict, Union

# def read_uiconfig(config_path: str) -> Dict[str, Any]:
#     """
#     Read UI configuration file (supports JSON and YAML formats).
    
#     Args:
#         config_path: Path to the configuration file
        
#     Returns:
#         Dictionary containing the configuration
#     """
#     path = Path(config_path)
    
#     if not path.exists():
#         raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
#     if path.suffix.lower() == '.json':
#         with open(path, 'r') as f:
#             return json.load(f)
#     elif path.suffix.lower() in ['.yaml', '.yml']:
#         with open(path, 'r') as f:
#             return yaml.safe_load(f)
#     else:
#         raise ValueError(f"Unsupported file format: {path.suffix}")


# def get_config_value(config: Dict[str, Any], key: str, default: Any = None) -> Any:
#     """
#     Get a value from config with dot notation support (e.g., 'ui.theme').
    
#     Args:
#         config: Configuration dictionary
#         key: Key to retrieve (supports dot notation)
#         default: Default value if key not found
        
#     Returns:
#         Configuration value or default
#     """
#     keys = key.split('.')
#     value = config
    
#     for k in keys:
#         if isinstance(value, dict):
#             value = value.get(k)
#             if value is None:
#                 return default
#         else:
#             return default
    
#     return value

from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfig.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)


    def get_llms(self):
       return self.config['DEFAULT'].get('LLM_MODELS').split(', ')
    
    def get_use_cases(self):
       return self.config['DEFAULT'].get('USE_CASES').split(', ')
    
    def get_page_title(self):
       return self.config['DEFAULT'].get('PAGE_TITLE')
    
    def get_groq_models(self):
       return self.config['DEFAULT'].get('GROQ_MODELS').split(', ')
    
    def get_openai_models(self):
       return self.config['DEFAULT'].get('OPENAI_MODELS').split(', ')
    
    def get_anthropic_models(self):
       return self.config['DEFAULT'].get('ANTHROPIC_MODELS').split(', ')