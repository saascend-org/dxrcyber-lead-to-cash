"""Inline src/ into build/index.plain.html (git-ignored; never commit it)."""
import pathlib
B = pathlib.Path(__file__).parent
S = B / 'src'
page = (S / 'page.html').read_text()
for marker, f in (('/*CSS*/', 'style.css'), ('/*DATA*/', 'data.js'), ('/*APP*/', 'app.js')):
    assert marker in page, marker
    page = page.replace(marker, (S / f).read_text())
(B / 'index.plain.html').write_text(page)
print(f'wrote build/index.plain.html ({len(page):,} bytes)')
