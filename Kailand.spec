# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('assets\\', 'assets')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Kailand',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='C:\\Users\\GATOAR~1\\AppData\\Local\\Temp\\ba0f75a6-475b-4b46-bd8e-305f7401fb9b',
    icon=['assets\\favicon.png'],
)
