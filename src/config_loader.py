import pathlib
import yaml
import logging,os

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

class ActionsConfig:
    def __init__(self, path:str="config/actions.yaml"):
        self.path = pathlib.Path(path)
        with self.path.open("r") as f:
            cfg= yaml.safe_load(f) or {}
        self.domain = cfg.get("domain")
        self.start = cfg.get("start")
        self.end_absorbing = cfg.get("end_absorbing")
        self.actions = cfg.get("actions",[])




