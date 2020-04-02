import importlib
import sys

test = "code/train/run_config.py"

spec = importlib.util.spec_from_file_location(
    name="trainingmodule",
    location=test
)
mod = importlib.util.module_from_spec(spec)
print(spec.loader.exec_module(mod))
print(mod)

function = getattr(mod, "main", None)
function()