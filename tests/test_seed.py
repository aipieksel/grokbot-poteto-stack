import importlib.util
import tempfile
import unittest
from pathlib import Path
spec = importlib.util.spec_from_file_location("seed", Path(__file__).resolve().parents[1] / "scripts/seed_os.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class SeedTests(unittest.TestCase):
    def test_seed_preserves_existing_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            destination = module.seed(project)
            self.assertEqual(len(list(destination.rglob("*.json"))), 4)
            goals = destination / "context/goals.md"
            goals.write_text("existing notes")
            with self.assertRaises(FileExistsError):
                module.seed(project)
            self.assertEqual(goals.read_text(), "existing notes")
    def test_destination_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "operating-system").symlink_to(project / "missing")
            with self.assertRaises(FileExistsError):
                module.seed(project)
            self.assertFalse((project / "missing").exists())
    def test_missing_project_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(FileNotFoundError):
                module.seed(Path(tmp) / "missing")
