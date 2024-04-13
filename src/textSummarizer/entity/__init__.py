from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
    