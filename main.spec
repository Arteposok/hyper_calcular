# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Artem\\OneDrive\\Рабочий стол\\hyper_calcular\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Artem\\OneDrive\\Рабочий стол\\hyper_calcular\\bold.ttf', '.'), ('C:\\Users\\Artem\\OneDrive\\Рабочий стол\\hyper_calcular\\font.ttf', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
)
