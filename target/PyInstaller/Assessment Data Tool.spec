# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\ojedalom\\cds_data_tool\\src\\main\\python\\lcc_assessment\\main.py'],
             pathex=['C:\\Users\\ojedalom\\cds_data_tool\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\ojedalom\\appdata\\local\\continuum\\miniconda3\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\ojedalom\\cds_data_tool\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Assessment Data Tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\ojedalom\\cds_data_tool\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Assessment Data Tool')
