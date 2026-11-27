"""Distribution membership, integrity and reproducibility regression tests."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location("profiles", Path(__file__).resolve().parents[1]/"tools/build_distribution_profiles.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

class TestProfiles(unittest.TestCase):
    def test_membership_and_repeatability(self):
        names = ["canonical/a.tex", "research_tracks/a.md", "research_fronts/b.md",
                 "ARCHIVE/old.tex", "docs/pdfs/a.pdf", "SHA256SUMS.txt",
                 "tools/build_distribution_profiles.py"]
        files = {n: ("100644",str(i)) for i,n in enumerate(names)}
        source = set(names)-{"docs/pdfs/a.pdf"}
        with tempfile.TemporaryDirectory() as d:
            base=Path(d)
            expected = {"core": {names[0],names[6]},
                        "research": {names[0],names[1],names[2],names[6]},
                        "full":set(names)}
            for profile in p.LIMITS:
                a,b=base/"a.zip",base/"b.zip"
                for target in (a,b):
                    p.write_zip(target,"test",profile,files,source,lambda oid: oid.encode())
                self.assertEqual(a.read_bytes(),b.read_bytes())
                with zipfile.ZipFile(a) as z:
                    self.assertEqual(set(z.namelist()),expected[profile]|{p.INDEX})

if __name__=="__main__":
    unittest.main()
